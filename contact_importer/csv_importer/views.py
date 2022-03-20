from django.views.generic import TemplateView, ListView
from .forms import csvFileForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from csv_importer.models import Contact, csvFile
from django.shortcuts import get_object_or_404

import datetime
import re

import pandas as pd

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"


@login_required
def file_upload(request):
    if request.method == 'POST':
        form = csvFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_csv_file = csvFile(file = request.FILES['file'])
            new_csv_file.user = request.user
            new_csv_file.name = request.POST['name']
            new_csv_file.save()
            return redirect('files')
    else:
        form = csvFileForm()
    
    context = {
        'form': form,
        # 'user': user
        }

    return render(request, 'upload_page.html', context)


class ListFiles(ListView, LoginRequiredMixin):
    model = csvFile
    paginate_by = 10
    template_name = "list_of_files.html"

    def get_queryset(self):
        return csvFile.objects.filter(user=self.request.user)



@login_required
def process_file(request, pk):
    file = get_object_or_404(csvFile, pk=pk)


    df = pd.read_csv(f"../contact_importer/media/{file.file}")
    df["date_of_birth"] = pd.to_datetime(df['date_of_birth'], format='%Y-%m-%d', errors='coerce')
    options = list(df.columns)
    

    if request.method == 'POST':
        for index, row in df.iterrows():
            if re.match("^[a-zA-Z -]*$", row[request.POST["name"]]):
                name = row[request.POST["name"]]
            else:
                name = None

            if isinstance(row[request.POST["date_of_birth"]], pd._libs.tslibs.timestamps.Timestamp):
                date_of_birth = row[request.POST["date_of_birth"]]
            else:
                date_of_birth = None

            if re.match("\(\+[0-9][0-9]\)[ ][0-9]{3}[ ][0-9]{3}[ ][0-9]{2}[ ][0-9]{2}[ ][0-9]{2}$|\(\+[0-9]{2}\)[ ][0-9]{3}[-][0-9]{3}[-][0-9]{2}[-][0-9]{2}[-][0-9]{2}$", row[request.POST["phone"]]):
                phone = row[request.POST["phone"]]
            else:
                phone = None
            
            if (pd.notnull(row[request.POST["address"]]) and row[request.POST["address"]] != ''):
                address = row[request.POST["address"]]
            else:
                address = None

            # contacts = Contact.objects.all()
            credit_card = row[request.POST["credit_card"]]
            franchise = row[request.POST["franchise"]]


            email = row[request.POST["email"]]

            new_ativo_instance = Contact.objects.create(name=name, date_of_birth=date_of_birth, phone=phone,
                                                        address=address, credit_card=credit_card, franchise=franchise, email=email)
            new_ativo_instance.save()




        # name = request.POST["name"]
        # date_of_birth = request.POST["date_of_birth"]
        # phone = request.POST["phone"]
        # address = request.POST["address"]
        # credit_card = request.POST["credit_card"]
        # franchise = request.POST["franchise"]
        # email = request.POST["email"]

        # new_ativo_instance = Contact.objects.create(name=name, date_of_birth=date_of_birth, phone=phone,
        #                                             address=address, credit_card=credit_card, franchise=franchise, email=email)
        # new_ativo_instance.save()

    context = {
        'file': file,
        'options': options,
    }

    return render(request, 'process_file.html', context)