from rest_framework import permissions
from .permissions import IstaffPermissions


class StaffEditorPermissionMixin():
    permission_classes=[permissions.IsAdminUser,IstaffPermissions]
