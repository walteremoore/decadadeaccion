from django.urls import path 
from . import views

app_name = "usuarios"

urlpatterns = [
	path("registrarme/", views.Registrarme.as_view(), name="registrarme"),
]