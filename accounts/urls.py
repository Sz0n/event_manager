from django.urls import path
from . import views


urlpatterns = [
    path("account/register/", views.RegisterView.as_view(), name="register"),
    path("account/login/", views.LoginView.as_view(), name="login"),
]
