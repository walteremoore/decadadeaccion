from django.urls    import path
from .              import views

app_name = "comentarios"

urlpatterns = [
    path('detalle/<int:pk>/', views.Detalle.as_view(), name="detalle"),

    #Admin
    path('admin/listar/', views.ListarAdmin.as_view(), name="admin_listar"),
    path('admin/nuevo/<aid>/', views.comentarioNuevo, name="admin_nuevo"),
    path('admin/editar/<int:pk>/', views.EditarAdmin.as_view(), name="admin_editar"),
    #path('admin/eliminar/<int:pk>/', views.EliminarAdmin.as_view(), name="admin_eliminar"),
    path('admin/eliminar/<aid>/', views.bajaLogicaCom, name="admin_eliminar"),
    path('admin/restaurar/<aid>/', views.restaurarCom, name="admin_restaurar"),
    path('admin/aprobar/<cid>/', views.aprobarCom, name="admin_aprobar"),
    path("miscomentarios/", views.MisComentarios.as_view(), name="mis_comentarios"),
]