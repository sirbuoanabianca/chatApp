from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from .models import User, BannedUser


def banMiddleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.user.is_authenticated:
            try:
                if request.user.banneduser.is_banned:
                    logout(request)
                    return JsonResponse({"message":"YOU ARE BANNED"},status=403)
            except ObjectDoesNotExist:
                pass

            
        elif request.method == 'POST':
            username = request.POST.get('username')
            if BannedUser.objects.all().filter(user__username=username).exists():
                status = BannedUser.objects.all().filter(user__username=username)[0].is_banned
                if(status):
                    return JsonResponse({"message":"YOU ARE BANNED"},status=403)
            
        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware