from django.views.generic import TemplateView, ListView
from .forms import csvFileForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from csv_importer.models import csvFile

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