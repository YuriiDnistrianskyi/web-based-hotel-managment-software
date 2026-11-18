import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from apps.user.services import auth_service, user_service

logger = logging.getLogger(__name__)


@login_required
@require_POST
def user_delete_view(request):
    try:
        user_id = request.user.id
        auth_service.logout(request)
        user_service.delete(user_id)
        return redirect('login')
    except Exception as ex:
        logger.error(f'Error: {ex}')
        return redirect('error')
