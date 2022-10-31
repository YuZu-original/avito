from rest_framework.permissions import BasePermission

from users.models import User


class SelectionEditPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.role in [User.MEMBER, User.ADMIN] or
                    request.user.id == obj.owner_id)


class AdEditPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.role in [User.MEMBER, User.ADMIN] or
                    request.user.id == obj.author_id)
