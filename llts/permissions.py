from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	Custom permission to only allow owners of an object to edit it.
	"""

	def has_object_permission(self, request, view, obj):
		# Read permissions are allowed to any request,
		# so we'll always allow GET, HEAD, or OPTIONS requests.
		if request.method in permission.SAFE_METHODS:
			return True

		return obj.owner == request.user

class IsOwner(permissions.BasePermission):
	"""
	Custom permission to only allow owners to see or edit thier own objects
	"""

	def has_object_permission(self, request, view, obj):

		return obj.owner == request.user