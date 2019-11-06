from django.contrib.admin import ModelAdmin


class AppelationAdmin(ModelAdmin):
    list_display = ['name', 'get_region_name', 'get_country_name']
    search_fields = ['name', 'region__name', 'region__country__name']
    raw_id_fields = ['region']

    def get_region_name(self, obj):
        return obj.region.name
    get_region_name.admin_order_field = 'region'
    get_region_name.short_description = 'Region Name'

    def get_country_name(self, obj):
        return obj.region.country.name
    get_country_name.admin_order_field = 'country'
    get_country_name.short_description = 'Country Name'


class RegionAdmin(ModelAdmin):
    list_display = ['name', 'get_country_name']
    search_fields = ['name', 'country__name']
    raw_id_fields = ['country']

    def get_country_name(self, obj):
        return obj.country.name
    get_country_name.admin_order_field = 'country'
    get_country_name.short_description = 'Country Name'


class CountryAdmin(ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
