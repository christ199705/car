from django.db import models


# Create your models here.


class Brand(models.Model):
    B_name = models.CharField(max_length=50, verbose_name="汽车品牌", unique=True, help_text="汽车品牌")
    country = models.CharField(max_length=50, verbose_name="发源国家", help_text="发源国家")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    originator = models.CharField(max_length=50, verbose_name="品牌创始人", help_text="品牌创始人")
    year_count = models.IntegerField(verbose_name="年销量", help_text="年销量")

    class Meta:
        db_table = "tb_brand"
        verbose_name = "汽车品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.B_name
