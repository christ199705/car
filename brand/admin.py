from django.contrib import admin
from . import models


# Register your models here.


class AdminBrand(admin.ModelAdmin):
    list_display = ["id", "B_name", "country", "originator","year_count","create_time", "update_time"]
    list_display_links = ["id", "B_name"]
    list_filter = ["country"]
    search_fields = ["id", "B_name"]
    list_editable = ["country", "originator"]


admin.site.register(models.Brand, AdminBrand)
