import json

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.mixins import RetrieveModelMixin, \
    UpdateModelMixin, DestroyModelMixin, ListModelMixin, CreateModelMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .serializers import CarBrandSerializers
# Create your views here.
from django.views import View
from .models import Brand


class CarBrand_1(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = Brand.objects.all()
    serializer_class = CarBrandSerializers
    # filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields = ["id", "B_name"]
    filterset_fields = ["id", "B_name"]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

        # query_brand = self.get_queryset()
        # brand = self.filter_queryset(query_brand)
        # page = self.paginate_queryset(brand)
        # if page is not None:
        #     serializer = self.get_serializer(instance=page, many=True)
        #     return self.get_paginated_response(serializer.data)
        # serializers = self.get_serializer(instance=brand, many=True)
        # return JsonResponse(serializers.data, safe=False)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        # serializers = self.get_serializer(data=request.data)
        # try:
        #     serializers.is_valid(raise_exception=True)
        # except Exception:
        #     return JsonResponse(serializers.errors, status=422)
        # serializers.save()
        # return JsonResponse(serializers.data, safe=False, status=201)


class CarBrand_2(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset = Brand.objects.all()
    serializer_class = CarBrandSerializers
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        # brand = self.get_object()
        # # try:
        # #     brand = Brand.objects.get(id=id)
        # # except Exception:
        # #     return JsonResponse({"error_code": 422, "error": "id不存在"}, status=status.HTTP_200_OK)
        # serializers = self.get_serializer(instance=brand)
        # return JsonResponse(serializers.data, safe=False)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        # brand = self.get_object()
        # serializers = self.get_serializer(instance=brand, data=request.data)
        # try:
        #     serializers.is_valid(raise_exception=True)
        # except Exception:
        #     return JsonResponse(serializers.errors, status=422)
        # serializers.save()
        # return JsonResponse(serializers.data, safe=False, status=201)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        # brand = self.get_object()
        # brand.delete()
        # return HttpResponse(1, status=204)
