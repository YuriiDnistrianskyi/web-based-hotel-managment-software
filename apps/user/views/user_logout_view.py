import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from apps.user.services import auth_service

logger = logging.getLogger(__name__)


@login_required
@require_POST
def user_logout_view(request):
    try:
        auth_service.logout(request)
        return redirect('login')
    except Exception as ex:
        logger.error(f'Erorr: {ex}')
        return redirect('error')
    