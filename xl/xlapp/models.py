from django.db import models


# Create your models here.
class Xlss(models.Model):
    API_WELL_NUMBER = models.IntegerField(null=True)
    QUARTER = models.IntegerField(null=True)
    OIL = models.IntegerField(null=True)
    GAS = models.IntegerField(null=True)
    BRINE = models.IntegerField(null=True)

    class Meta:
        db_table = 'Xlss'


class Sum(models.Model):
    API_WELL_NUMBER = models.IntegerField(null=True)
    OIL = models.IntegerField(null=True)
    GAS = models.IntegerField(null=True)
    BRINE = models.IntegerField(null=True)

    class Meta:
        db_table = 'Sum'
