from django.core.exceptions import PermissionDenied
class AdminRequiredMixins():
	# permisos_requeridos = []


	def dispatch(self, request, *args, **kwars):
		# print(self.permisos_requeridos)
		if not request.user.es_administrador:
			raise PermissionDenied
		return super(AdminRequiredMixins, self).dispatch(request, *args, **kwars)