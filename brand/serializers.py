from rest_framework import serializers
from .models import Brand
from rest_framework.validators import UniqueValidator


def test_validate(country):
    # "外部校验器"
    if country not in ["中国", "日本", "美国"]:
        raise serializers.ValidationError("汽车品牌错误")


class CarBrandSerializers_2(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    B_name = serializers.CharField(max_length=50, min_length=1,
                                   validators=[UniqueValidator(queryset=Brand.objects.all(), message="该品牌已经存在")])
    originator = serializers.CharField(max_length=50, min_length=1, help_text="品牌创始人")
    country = serializers.CharField(max_length=50, min_length=1, help_text="国家", validators=[test_validate])
    year_count = serializers.IntegerField(max_value=100000000, min_value=0, help_text="年销量", write_only=True)

    def create(self, validated_data):
        return Brand.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.B_name = validated_data["B_name"]
        instance.country = validated_data["country"]
        instance.originator = validated_data["originator"]
        instance.year_count = validated_data["year_count"]
        instance.save()
        return instance

    def validate(self, attrs):
        if attrs["originator"] == "黄婉如":
            raise serializers.ValidationError("黄婉如不存在")
        if attrs["B_name"] == "黄婉如":
            raise serializers.ValidationError("姓名不能为黄婉如")
        return attrs


"""
    def validate_country(self, value):
        # "单字段校验器"
        if value not in ["中国", "日本", "美国"]:
            raise serializers.ValidationError("汽车品牌a错误")
        return value
"""
"`````````````````````````````````````````````````````````````````````````````````````````````````````````````"
"""
最终的版本，序例化器
"""


class CarBrandSerializers(serializers.ModelSerializer):
    type_set = serializers.StringRelatedField(many=True)
    class Meta:
        model = Brand
        # 所有字段
        # fields = "__all__"
        # 指定字段
        # fields = "name"
        # 指定字段排除
        exclude = ("create_time", "update_time")
        read_only_fields = ["id"]
        extra_kwargs = {
            "B_name": {
                "validators": [UniqueValidator(queryset=Brand.objects.all(), message="该品牌已经存在")]
            },
            "year_count": {"write_only": True}
        }

    def validate(self, attrs):
        if attrs["originator"] == "黄婉如":
            raise serializers.ValidationError("黄婉如不存在")
        if attrs["B_name"] == "黄婉如":
            raise serializers.ValidationError("姓名不能为黄婉如")
        return attrs
