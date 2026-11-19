import logging

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from apps.user.services import auth_service, user_service

logger = logging.getLogger(__name__)


@login_required
@require_POST
def user_delete_view(request):
    user_id = request.user.id
    with transaction.atomic():
        user_service.delete(user_id)
    auth_service.logout(request)
    return redirect('login')
