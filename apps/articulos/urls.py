from django.urls    import path
from .              import views

app_name = "articulos"

urlpatterns = [
    path('detalle/<int:pk>/', views.Detalle.as_view(), name="detalle"),

    #Admin
    path('admin/listar/', views.ListarAdmin.as_view(), name="admin_listar"),
    path('admin/nuevo/', views.NuevoAdmin.as_view(), name="admin_nuevo"),
    path('admin/editar/<int:pk>/', views.EditarAdmin.as_view(), name="admin_editar"),
    #path('admin/eliminar/<int:pk>/', views.EliminarAdmin.as_view(), name="admin_eliminar"),
    #path('admin/eliminar/<int:pk>/', views.BorrarLogicoAdmin.as_view(), name="admin_eliminar"),
    path('admin/eliminar/<aid>/', views.bajaLogica, name="admin_eliminar"),
    path('admin/eliminar/<aid>/', views.restaurarArticulo, name="admin_restaurar"),
    path("misarticulos/", views.MisArticulos.as_view(), name="mis_articulos")
]