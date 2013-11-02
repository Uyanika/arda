# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Destinations(models.Model):
    id = models.IntegerField(primary_key=True)
    cityname = models.TextField(db_column='CityName', blank=True) # Field name made lowercase. This field type is a guess.
    airport = models.TextField(db_column='Airport', blank=True) # Field name made lowercase. This field type is a guess.
    lat = models.TextField(db_column='Lat', blank=True) # Field name made lowercase. This field type is a guess.
    lon = models.TextField(db_column='Lon', blank=True) # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = 'destinations'

