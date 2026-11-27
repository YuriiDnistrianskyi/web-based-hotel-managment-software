from apps.user.constants import ConstUserRole

from .role_required_mixin import RoleRequiredMixin


class UserRequiredMixin(RoleRequiredMixin):
    allowed_roles = [ConstUserRole.USER]
