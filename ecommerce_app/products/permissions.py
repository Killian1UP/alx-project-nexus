from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow only admins to create, update, or delete objects.
    Authenticated users can only read (GET, HEAD, OPTIONS).
    """

    def has_permission(self, request, view):
        # Safe methods are GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        # For other methods, user must be admin
        return request.user.is_authenticated and request.user.role == 'admin'