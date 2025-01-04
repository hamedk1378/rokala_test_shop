from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsAdminUserOrReadOnly(BasePermission):
    """
    Allows access to authenticated admin users
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or\
            bool(request.user and request.user.is_authenticated and request.user.is_admin):
            return True
        else:
            return False