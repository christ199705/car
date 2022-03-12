import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .serializers import CarBrandSerializers
# Create your views here.
from django.views import View
from .models import Brand


class CarBrand_1(View):
    def get(self, request):
        brand = Brand.objects.all()
        serializers = CarBrandSerializers(instance=brand, many=True)
        return JsonResponse(serializers.data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        serializers = CarBrandSerializers(data=data)
        try:
            serializers.is_valid(raise_exception=True)
        except Exception:
            return JsonResponse(serializers.errors, status=422)
        serializers.save()
        print(serializers.data)
        return JsonResponse(serializers.data, safe=False, status=201)


class CarBrand_2(View):
    def get(self, request, id):
        try:
            brand = Brand.objects.get(id=id)
        except Exception:
            return JsonResponse({"error_code": 422, "error": "id不存在"}, status=422)
        serializers = CarBrandSerializers(instance=brand)
        return JsonResponse(serializers.data, safe=False)

    def put(self, request, id):
        try:
            brand = Brand.objects.get(id=id)
        except Exception:
            return JsonResponse({"error_code": 422, "error": "id不存在"}, status=422)
        data = json.loads(request.body)
        serializers = CarBrandSerializers(instance=brand, data=data)
        try:
            serializers.is_valid(raise_exception=True)
        except Exception:
            return JsonResponse(serializers.errors, status=422)
        serializers.save()
        return JsonResponse(serializers.data, safe=False, status=201)

    def delete(self, request, id):
        try:
            brand = Brand.objects.get(id=id)
        except Exception:
            return JsonResponse({"error_code": 422, "error": "id不存在"}, status=422)
        brand.delete()
        return HttpResponse(1, status=204)
