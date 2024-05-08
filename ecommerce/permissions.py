from rest_framework import BasePermission

class CanDeleteProduct(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.method == 'DELETE'