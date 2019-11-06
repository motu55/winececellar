from django.contrib import admin

from winecellar.admins import BaseAdmin
from winecellar.admins.bottles import BottleAdmin
from winecellar.admins.origins import AppelationAdmin, RegionAdmin, CountryAdmin
from winecellar.admins.wine import WineAdmin
from winecellar.models import Appelation, Vendor, Bottle, BottleArchive, Country, Shelf, Region, GrapeVariety, Wine, \
    Producer

admin.site.register(Appelation, AppelationAdmin)
admin.site.register(Vendor, BaseAdmin)
admin.site.register(Bottle, BottleAdmin)
admin.site.register(BottleArchive, BottleAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Shelf, BaseAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(GrapeVariety, BaseAdmin)
admin.site.register(Wine, WineAdmin)
admin.site.register(Producer, BaseAdmin)
