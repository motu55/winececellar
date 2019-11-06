# Generated by Django 2.2.7 on 2019-11-06 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GrapeVariety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('url', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='winecellar.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('uid', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('url', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('url', models.TextField(blank=True, null=True)),
                ('minyears', models.FloatField(blank=True, null=True)),
                ('maxyears', models.FloatField(blank=True, null=True)),
                ('appelation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='winecellar.Appelation')),
                ('producer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='winecellar.Producer')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='winecellar.Region')),
            ],
        ),
        migrations.CreateModel(
            name='MadeFrom',
            fields=[
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='winecellar.Wine')),
                ('grapevariety', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='winecellar.GrapeVariety')),
            ],
        ),
        migrations.CreateModel(
            name='BottleArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vintage', models.IntegerField(blank=True, null=True)),
                ('volume', models.FloatField()),
                ('price', models.FloatField()),
                ('shelf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='winecellar.Shelf')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='winecellar.Vendor')),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='winecellar.Wine')),
            ],
        ),
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vintage', models.IntegerField(blank=True, null=True)),
                ('volume', models.FloatField()),
                ('price', models.FloatField()),
                ('shelf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='winecellar.Shelf')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='winecellar.Vendor')),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='winecellar.Wine')),
            ],
        ),
        migrations.AddField(
            model_name='appelation',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='winecellar.Region'),
        ),
        migrations.AddField(
            model_name='wine',
            name='varieties',
            field=models.ManyToManyField(through='winecellar.MadeFrom', to='winecellar.GrapeVariety'),
        ),
    ]
