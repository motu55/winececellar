from django.contrib.admin import ModelAdmin


class BaseAdmin(ModelAdmin):
    search_fields = ['name']
