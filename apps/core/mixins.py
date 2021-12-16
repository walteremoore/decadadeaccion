from django.core.exceptions import PermissionDenied
class AdminRequiredMixins():

	def dispatch(self, request, *args, **kwars):
		if not request.user.es_administrador:
			raise PermissionDenied
		return super(AdminRequiredMixins, self).dispatch(request, *args, **kwars)