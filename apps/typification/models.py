from django.db import models

from apps.campaign.models import Contact


class Evaluation(models.Model):
    class TypeEvaluation(models.TextChoices):
        default = 'pendiente'
        positive = 'positivo'
        negative = 'negativo'
        not_wanted = 'no deseado'
        verify_number = 'verificar número'
        not_apply = 'no aplica'

    type_evaluation = models.CharField(
        max_length=50, choices=TypeEvaluation.choices, default=TypeEvaluation.default)
    coment = models.TextField(blank=True, null=True)
    contact = models.ForeignKey(
        Contact, related_name='contact_type_evaluation', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Evaluación'
        verbose_name_plural = 'Evaaluaciones'
        ordering = ('-updated_at',)

    def __str__(self):
        return self.contact.name
