from rest_framework import serializers
from brand.serializers import CarBrandSerializers
from brand.models import Brand
from .models import Type


class TypeSerializers(serializers.ModelSerializer):
    brand_name = serializers.StringRelatedField(label="所属品牌")
    # brand = serializers.SlugRelatedField(label="所属品牌",slug_field="B_id",queryset=Brand.objects.all())
    # B_name = CarBrandSerializers(read_only=True)

    class Meta:
        model = Type
        exclude = ("create_time", "update_time")
        read_only_fields = ("id",)
        extra_kwargs = {
            "name": {"max_length": 10, "min_length": 2,
                     "error_messages": {"max_length": "最大长度10", "min_length": "最小长度2"}},
            # "brand": {"write_only": True},
            "up_time": {"write_only": True}

        }

