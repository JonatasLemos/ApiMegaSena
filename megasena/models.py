from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class SorteioMegaSena(models.Model):
    dezena1 = models.PositiveSmallIntegerField()
    dezena2 = models.PositiveSmallIntegerField()
    dezena3 = models.PositiveSmallIntegerField()
    dezena4 = models.PositiveSmallIntegerField()
    dezena5 = models.PositiveSmallIntegerField()
    dezena6 = models.PositiveSmallIntegerField()
    date = models.DateTimeField()

class NovoJogo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dezena1 = models.PositiveSmallIntegerField()
    dezena2 = models.PositiveSmallIntegerField()
    dezena3 = models.PositiveSmallIntegerField()
    dezena4 = models.PositiveSmallIntegerField()
    dezena5 = models.PositiveSmallIntegerField()
    dezena6 = models.PositiveSmallIntegerField()
    dezena7 = models.PositiveSmallIntegerField(null=True)
    dezena8 = models.PositiveSmallIntegerField(null=True)
    dezena9 = models.PositiveSmallIntegerField(null=True)
    dezena10 = models.PositiveSmallIntegerField(null=True)
    dezenas = models.PositiveSmallIntegerField(choices=[(i,f'{i} dezena(s)') for i in range(1,11)])
    acertos = models.PositiveSmallIntegerField()
    date = models.DateTimeField(default=timezone.now)
