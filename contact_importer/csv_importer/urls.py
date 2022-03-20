from django.urls import path
from csv_importer.views import IndexView, ListFiles
from . import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("upload", views.file_upload, name="upload"),
    path("files", ListFiles.as_view(), name="files"),
    path("process/<int:pk>", views.process_file, name="process"),
]