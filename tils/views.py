import jsend
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Til
from .serializers import TilSerializer


class TilList(GenericAPIView):
    serializer_class = TilSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        tils = Til.objects.filter(owner=request.user)
        serializer = TilSerializer(tils, many=True)
        res = jsend.success(data={"tils": serializer.data})
        return Response(res)

    def post(self, request, format=None):
        serializer = TilSerializer(data=request.data)
        if serializer.is_valid() == False:
            res = jsend.fail(data=serializer.errors)
            return Response(res)

        serializer.save(owner=request.user)
        res = jsend.success(data={"detail": _("Successfully registered.")})
        return Response(res)


class TilDetail(GenericAPIView):
    serializer_class = TilSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, til_id):
        til = Til.objects.get(pk=til_id)
        return til

    def get(self, request, til_id, format=None):
        try:
            til = self.get_object(til_id)
        except:
            res = jsend.fail(data={"detail": _("This is not a registered")})
            return Response(res)

        serializer = TilSerializer(til)
        res = jsend.success(data=serializer.data)
        return Response(res)

    def put(self, request, til_id, format=None):
        try:
            til = self.get_object(til_id)
        except:
            res = jsend.fail(data={"detail": _("This is not a registered")})
            return Response(res)

        serializer = TilSerializer(til, data=request.data)
        if serializer.is_valid() == False:
            res = jsend.fail(data=serializer.errors)
            return Response(res)
        serializer.save()
        res = jsend.success(data={"detail": _("Successfully modified.")})
        return Response(res)

    def delete(self, request, til_id, format=None):
        try:
            til = self.get_object(til_id)
        except:
            res = jsend.fail(data={"detail": _("This is not a registered")})
            return Response(res)

        til.delete()
        res = jsend.success(data={"detail": _("Successfully deleted.")})
        return Response(res)
