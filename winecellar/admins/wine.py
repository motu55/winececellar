from django.contrib.admin import ModelAdmin


class WineAdmin(ModelAdmin):
    list_display = ['name', 'get_producer_name', 'get_appelation_name', 'get_region_name', 'get_country_name']
    search_fields = ['name', 'producer__name', 'appelation__name', 'appelation__region__name']
    raw_id_fields = ['producer', 'appelation']

    def get_producer_name(self, obj):
        if obj.producer:
            return obj.producer.name
        return ''
    get_producer_name.admin_order_field = 'producer'
    get_producer_name.short_description = 'Producer Name'

    def get_region_name(self, obj):
        if obj.appelation:
            return obj.appelation.region.name
        return ''
    get_region_name.admin_order_field = 'region'
    get_region_name.short_description = 'Region Name'

    def get_appelation_name(self, obj):
        if obj.appelation:
            return obj.appelation.name
        return ''
    get_appelation_name.admin_order_field = 'appelation'
    get_appelation_name.short_description = 'Appelation Name'

    def get_country_name(self, obj):
        if obj.appelation:
            return obj.appelation.region.country.name
        return ''
    get_country_name.admin_order_field = 'country'
    get_country_name.short_description = 'Country Name'
