from rest_framework import permissions

class IsPlayerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only access to any user
        if request.method in permissions.SAFE_METHODS:
            return True
        # Check if the user is the same as the player
        return obj.player == request.user

# Only Profile (read_only) or Admin can have access
class IsProfileOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow administrators full access
        if request.user.is_staff:
            return True

        # Allow users to view their own profile (read-only)
        if request.method in permissions.SAFE_METHODS and obj == request.user.player:
            return True

        return False
