import jsend
from django.conf import settings
from django.contrib.auth import login as django_login, logout as django_logout
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _

from rest_framework import response
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_auth.views import LoginView, LogoutView

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
class UserCheck(APIView):
    def get(self, request, email, format=None):
        email = CustomUser.objects.filter(email=email)
        serializer = UserCheckSerializer(email)
        res = jsend.success(data=serializer.data)
        return Response(res)


# rest_auth.views.LoginView overriding
class LoginView(LoginView):
    def get_response(self):
        serializer_class = self.get_response_serializer()

        if getattr(settings, "REST_USE_JWT", False):
            data = {"user": self.user, "token": self.token}
            serializer = serializer_class(
                instance=data, context={"request": self.request}
            )
        else:
            serializer = serializer_class(
                instance=self.token, context={"request": self.request}
            )

        res = jsend.success(data=serializer.data)  # jsend 적용
        response = Response(res, status=status.HTTP_200_OK)
        if getattr(settings, "REST_USE_JWT", False):
            from rest_framework_jwt.settings import api_settings as jwt_settings

            if jwt_settings.JWT_AUTH_COOKIE:
                from datetime import datetime

                expiration = datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA
                response.set_cookie(
                    jwt_settings.JWT_AUTH_COOKIE,
                    self.token,
                    expires=expiration,
                    httponly=True,
                )
        return response

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(
            data=self.request.data, context={"request": request}
        )
        if self.serializer.is_valid(raise_exception=False) == False:
            res = jsend.fail(data=self.serializer.errors)  # jsend 적용
            return Response(res)

        self.login()
        return self.get_response()


# rest_auth.views.LogoutView overriding
class LogoutView(LogoutView):
    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        if getattr(settings, "REST_SESSION_LOGIN", True):
            django_logout(request)

        res = jsend.success(data={"detail": _("Successfully logged out.")})  # jsend 적용
        response = Response(res, status=status.HTTP_200_OK)
        if getattr(settings, "REST_USE_JWT", False):
            from rest_framework_jwt.settings import api_settings as jwt_settings

            if jwt_settings.JWT_AUTH_COOKIE:
                response.delete_cookie(jwt_settings.JWT_AUTH_COOKIE)
        return response
