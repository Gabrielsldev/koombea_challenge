from django.urls import path
from .views import IndexView
from . import views


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]