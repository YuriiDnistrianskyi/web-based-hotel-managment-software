from apps.user.constants import ConstUserRole

from .role_required_mixin import RoleRequiredMixin


class AdminRequiredMixin(RoleRequiredMixin):
    allowed_roles = [ConstUserRole.ADMIN]
