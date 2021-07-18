from django.db import models

class SorteioMegaSena(models.Model):
    dezena1 = models.PositiveSmallIntegerField()
    dezena2 = models.PositiveSmallIntegerField()
    dezena3 = models.PositiveSmallIntegerField()
    dezena4 = models.PositiveSmallIntegerField()
    dezena5 = models.PositiveSmallIntegerField()
    dezena6 = models.PositiveSmallIntegerField()
    date = models.DateTimeField()
