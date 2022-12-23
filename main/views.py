from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .serializers import *
from .models import *


# Create your views here.

class PlanList(APIView):
    def get(self, request):
        queryset = Plan.objects.all()
        serializer = PlanSerializer(
            queryset, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PlanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
