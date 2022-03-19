from django.views.generic import TemplateView
from .forms import csvFileForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = csvFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = csvFileForm()
    return render(request, 'upload_page.html',{'form': form})