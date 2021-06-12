from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_auth.views import LoginView

from .serializers import CustomUser


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "login": reverse("rest_login", request=request, format=format),
            "logout": reverse("rest_logout", request=request, format=format),
            "password_change": reverse(
                "rest_password_change", request=request, format=format
            ),
            "password_reset": reverse(
                "rest_password_reset", request=request, format=format
            ),
            "register": reverse("rest_register", request=request, format=format),
            "logged_in_user": reverse(
                "rest_user_details", request=request, format=format
            ),
        }
    )
