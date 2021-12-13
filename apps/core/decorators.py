from django.core.exceptions import PermissionDenied


def admin_required():
	def deco_permission(f):
		def check(request, *args, **kwargs):
			if not request.user.es_administrador:
				raise PermissionDenied
			return f(request, *args, **kwargs)
		return check
	return deco_permission