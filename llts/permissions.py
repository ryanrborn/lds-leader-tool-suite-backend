from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	Custom permission to only allow owners of an object to edit it.
	"""

	def has_object_permission(self, request, view, obj):
		# Read permissions are allowed to any request,
		# so we'll always allow GET, HEAD, or OPTIONS requests.
		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.owner == request.user

class IsOwner(permissions.BasePermission):
	"""
	Custom permission to only allow owners to see or edit thier own objects
	"""

	def has_object_permission(self, request, view, obj):

		return obj.owner == request.user

class AnyCreateOwnerSeeEdit(permissions.BasePermission):
	"""
	Custom permission that allows anyone to create a new object, but only 
	owners can see and edit them
	"""

	def has_object_permission(self, request, view, obj):

		if request.method == "GET" or request.method == "PUT":
			return obj.owner == request.user
		return True

class OwnerOrAdmin(permissions.BasePermission):
	"""
	Custom permission that allows only the owner or admin to view
	objects
	"""

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or obj.owner == request.user:
			return True
		return False