from rest_framework import permissions

class IsPlayerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only access to any user
        if request.method in permissions.SAFE_METHODS:
            return True
        # Check if the user is the same as the player
        return obj.player == request.user
