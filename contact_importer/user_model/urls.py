from django.urls import path
from .views import SignUpView
from . import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', views.signin, name='signin'),
    path("logout", views.logout_user, name="logout"),
]