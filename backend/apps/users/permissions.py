from backend.core import permissions


def has_permission(request, view):
    if request.user.is_authenticated and request.user.is_staff:
        return True
    return False


class IsAdminOrHasRole(permissions.BasePermission):
    pass