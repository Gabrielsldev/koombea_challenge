from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from .forms import csvFileForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from csv_importer.models import Contact, csvFile
from django.shortcuts import get_object_or_404
import logging

import pandas as pd

from csv_importer.utils.validation_rules import validate_csv_fields

logger = logging.getLogger(__name__)

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"


# View to upload a file
@login_required
def file_upload(request):
    if request.method == 'POST':
        form = csvFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_csv_file = csvFile(file = request.FILES['file'])
            new_csv_file.user = request.user
            new_csv_file.name = request.POST['name']
            new_csv_file.on_hold = True
            new_csv_file.save()
            return redirect('files')
    else:
        form = csvFileForm()
    
    context = {
        'form': form,
        # 'user': user
        }

    return render(request, 'upload_page.html', context)


# View to list all files per user
class ListFiles(ListView, LoginRequiredMixin):
    model = csvFile
    paginate_by = 10
    template_name = "list_of_files.html"

    def get_queryset(self):
        return csvFile.objects.filter(user=self.request.user)



@login_required
def process_file(request, pk):
    file = get_object_or_404(csvFile, pk=pk)

    # Read CSV file
    df = pd.read_csv(f"../contact_importer/media/{file.file}")
    options = list(df.columns)

    if request.method == 'POST':
        # Function to validate CSV fields
        validate_csv_fields(request, file, df)
        return HttpResponseRedirect(reverse('contact'))

    context = {
        'file': file,
        'options': options,
    }

    return render(request, 'process_file.html', context)


# View to list all contacts per user
class ListContacts(ListView, LoginRequiredMixin):
    model = Contact
    paginate_by = 10
    template_name = "list_of_contacts.html"

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)