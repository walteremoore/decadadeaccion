from django.urls    import path
from .              import views

app_name = "articulos"

urlpatterns = [
    path('detalle/', views.detalle, name="detalle"),

    #Admin
    path('admin/listar/', views.ListarAdmin.as_view(), name="admin_listar"),
    path('admin/nuevo/', views.NuevoAdmin.as_view(), name="admin_nuevo"),
    path('admin/editar/<int:pk>/', views.EditarAdmin.as_view(), name="admin_editar"),
    path('admin/eliminar/<int:pk>/', views.EliminarAdmin.as_view(), name="admin_eliminar"),
    path("misarticulos/", views.MisArticulos.as_view(), name="mis_articulos")
]