from rest_framework import permissions
from .permissions import IstaffPermissions


class StaffEditorPermissionMixin():
    permission_classes=[permissions.IsAdminUser,IstaffPermissions]

class UserGetQuerySetProductMixin():
    user_field="user"
    def get_queryset(self,*args, **kwargs):
        qs=super().get_queryset(*args, **kwargs)
        query_data={}
        query_data[self.user_field]=self.request.user

        return qs.filter(**query_data)
