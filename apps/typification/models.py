from django.db import models

from apps.campaign.models import Contact


class Evaluation(models.Model):
    class TypeEvaluation(models.TextChoices):
        default = 'pendiente'
        positive = 'positivo'
        negative = 'negativo'
        not_wanted = 'no deseado'
        verify_number = 'verificar número'
        not_apply= 'no aplica'


    type = models.CharField(
        max_length=50, choices=TypeEvaluation.choices, default=TypeEvaluation.default)
    coment = models.TextField(blank=True, null=True)
    contact = models.ForeignKey(Contact, related_name='contact')
