from django.shortcuts import render, get_object_or_404
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


class PlanDetail(APIView):
    def get(self, request, id):
        plan = get_object_or_404(Plan, pk=id)
        serializer = PlanSerializer(plan)
        return Response(serializer.data)

    def put(self, request, id):
        plan = get_object_or_404(Plan, pk=id)
        serializer = PlanSerializer(plan, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        plan = get_object_or_404(Plan, pk=id)
        if product.members.count() > 0:
            return Response({'detail': 'Cannot delete plan with active members'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagList(APIView):
    def get(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(
            queryset, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TagDetail(APIView):
    def get(self, request, id):
        tag = get_object_or_404(Tag, pk=id)
        serializer = TagSerializer(Tag)
        return Response(serializer.data)

    def put(self, request, id):
        tag = get_object_or_404(Tag, pk=id)
        serializer = TagSerializer(Tag, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        tag = get_object_or_404(Tag, pk=id)
        if tags.plans.count() > 0:
            return Response({'detail': 'Cannot delete plan with active members'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
