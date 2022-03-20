from django.views.generic import TemplateView, ListView
from .forms import csvFileForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from csv_importer.models import Contact, csvFile
from django.shortcuts import get_object_or_404

import datetime

import pandas as pd

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"


@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = csvFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('files')
    else:
        form = csvFileForm()
    return render(request, 'upload_page.html',{'form': form})


class ListFiles(ListView, LoginRequiredMixin):
    model = csvFile
    paginate_by = 10
    template_name = "list_of_files.html"


@login_required
def process_file(request, pk):
    file = get_object_or_404(csvFile, pk=pk)


    df = pd.read_csv("../contact_importer/media/csvfiles/2022/03/contacts_test.csv")
    options = list(df.columns)
    

    if request.method == 'POST':
        for index, row in df.iterrows():
            name = row[request.POST["name"]]
            date_of_birth = row[request.POST["date_of_birth"]]
            phone = row[request.POST["phone"]]
            address = row[request.POST["address"]]
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