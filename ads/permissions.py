from rest_framework.permissions import BasePermission

from users.models import User


class SelectionEditPermission(BasePermission):
    message = "It's not your selection!"

    def has_object_permission(self, request, view, obj):
        return bool(request.user.role in [User.MODERATOR, User.ADMIN] or
                    request.user.id == obj.owner_id)


class AdEditPermission(BasePermission):
    message = "It's not your ad!"

    def has_object_permission(self, request, view, obj):
        return bool(request.user.role in [User.MODERATOR, User.ADMIN] or
                    request.user.id == obj.author_id)
