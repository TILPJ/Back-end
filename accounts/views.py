from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "login": reverse("api_login", request=request, format=format),
            "logout": reverse("api_logout", request=request, format=format),
            "password_change": reverse(
                "api_password_change", request=request, format=format
            ),
            "register": reverse("api_register", request=request, format=format),
        }
    )
