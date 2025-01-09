from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    """Разрешает доступ только активным пользователям"""

    def has_permission(self, request, view):
        return request.user.is_active