from django.contrib.admin import ModelAdmin


class BottleAdmin(ModelAdmin):
    list_display = ['__str__', 'vintage', 'volume']
    search_fields = ['__str__', 'vintage', 'volume']
    raw_id_fields = ['wine', 'vendor']
