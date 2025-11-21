from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Пользователи могут смотреть список книг.
    Только админы (is_staff=True) могут добавлять или удалять книги.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return request.user and request.user.is_staff
