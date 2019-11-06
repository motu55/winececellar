from django.db import models


class Appelation(models.Model):
    region = models.ForeignKey('Region', models.PROTECT)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=250)
    url = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Bottle(models.Model):
    wine = models.ForeignKey('Wine', models.PROTECT)
    vendor = models.ForeignKey(Vendor, models.PROTECT, blank=True, null=True)
    vintage = models.IntegerField(blank=True, null=True)
    volume = models.FloatField()
    price = models.FloatField()
    shelf = models.ForeignKey('Shelf', models.PROTECT)

    def __str__(self):
        return self.wine.name


class BottleArchive(models.Model):
    wine = models.ForeignKey('Wine', models.PROTECT)
    vendor = models.ForeignKey(Vendor, models.PROTECT, blank=True, null=True)
    vintage = models.IntegerField(blank=True, null=True)
    volume = models.FloatField()
    price = models.FloatField()
    shelf = models.ForeignKey('Shelf', models.PROTECT)

    def __str__(self):
        return self.wine.name


class Country(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.name


class Shelf(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Region(models.Model):
    country = models.ForeignKey(Country, models.PROTECT)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class GrapeVariety(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Wine(models.Model):
    producer = models.ForeignKey('Producer', models.PROTECT, blank=True, null=True)
    appelation = models.ForeignKey(Appelation, models.PROTECT, blank=True, null=True)
    name = models.CharField(max_length=250)
    url = models.TextField(blank=True, null=True)
    minyears = models.FloatField(blank=True, null=True)
    maxyears = models.FloatField(blank=True, null=True)
    varieties = models.ManyToManyField(
        'GrapeVariety',
        through='MadeFrom',
        through_fields=('wine', 'grapevariety'),
    )

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField(max_length=250)
    url = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class MadeFrom(models.Model):
    wine = models.ForeignKey(Wine, models.PROTECT)
    grapevariety = models.ForeignKey(GrapeVariety, models.PROTECT)
