from django.urls import path
from .views import IndexView, model_form_upload, ListFiles
from . import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("upload", views.model_form_upload, name="upload"),
    path("files", ListFiles.as_view(), name="files"),
]