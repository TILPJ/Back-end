import jsend

from rest_framework import response
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import UserCheckSerializer


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


# 회원 여부 체크
# class UserCheck(APIView):
#     def get(self, request, email, format=None):
#         email = CustomUser.objects.filter(email=email)
#         serializer = UserCheckSerializer(email)
#         return Response(serializer.data)


class UserCheck(APIView):
    def get(self, request, email, format=None):
        email = CustomUser.objects.filter(email=email)
        serializer = UserCheckSerializer(email)
        res = jsend.success(data=serializer.data)
        return Response(res)
