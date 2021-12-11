from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    #path('inicio/', views.Inicio, name="inicio"),
    path('inicio/', views.Inicio.as_view(), name="inicio"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.logout_then_login, name="logout"),
    #Includes
    path('articulos/', include('apps.articulos.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)