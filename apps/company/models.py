from django.utils.crypto import get_random_string
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Company(models.Model):
    name = models.CharField(max_length=100)
    pool_user = models.ManyToManyField(
        User,  related_name='users')
    token = models.CharField(max_length=40,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Compania'
        verbose_name_plural = 'Companias'
        ordering = ('-updated_at',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            to_assign = get_random_string(length=30)
            if Company.objects.filter(token=to_assign).exists():
                to_assign = to_assign+str(Company.objects.all().count())
            self.token = to_assign
        super().save(*args, **kwargs)
