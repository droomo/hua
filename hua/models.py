from __future__ import unicode_literals

from django.db import models


class Driver(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    update_at = models.DateTimeField()
    driver_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'driver'