from django.db import models


class Balance(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f'balace: {self.balance}'


class Promocode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.code
