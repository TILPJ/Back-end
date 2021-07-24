import jsend
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from .models import MyCourse
from .serializers import MyCourseSerializer


class MyCourseList(GenericAPIView):
    serializer_class = MyCourseSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        mycourse = MyCourse.objects.filter(owner=request.user)
        serializer = MyCourseSerializer(mycourse, many=True)
        res = jsend.success(data={"mycourses": serializer.data})
        return Response(res)

    def post(self, request, format=None):
        serializer = MyCourseSerializer(data=request.data)
        if serializer.is_valid() == False:
            res = jsend.fail(data=serializer.errors)
            return Response(res)

        serializer.save(owner=request.user)
        res = jsend.success(data={"detail": _("Successfully registered.")})
        return Response(res)


class MyCourseDetail(GenericAPIView):
    serializer_class = MyCourseSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, mycourse_id):
        mycourse = MyCourse.objects.get(pk=mycourse_id)
        return mycourse

    def get(self, request, mycourse_id, format=None):
        try:
            mycourse = self.get_object(mycourse_id)
        except:
            res = jsend.fail(data={"detail": _("This is not a registered")})
            return Response(res)

        serializer = MyCourseSerializer(mycourse)
        res = jsend.success(data=serializer.data)
        return Response(res)

    def delete(self, request, mycourse_id, format=None):
        try:
            mycourse = self.get_object(mycourse_id)
        except:
            res = jsend.fail(data={"detail": _("This is not a registered")})
            return Response(res)

        mycourse.delete()
        res = jsend.success(data={"detail": _("Successfully deleted.")})
        return Response(res)
