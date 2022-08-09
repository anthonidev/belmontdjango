from django.db import models
from django.template.defaultfilters import slugify


class Client(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, unique=True)
    # address = models.CharField(max_length=255)
    # city = models.CharField(max_length=255)
    # country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ('-updated_at',)

    def __str__(self):
        return self.name

    def get_fullname(self):
        return self.name + " " + self.lastname

    def save(self, *args, **kwargs):
        if not self.id:
            to_assign = slugify(self.name+self.lastname)
            if Client.objects.filter(slug=to_assign).exists():
                to_assign = to_assign+str(Client.objects.all().count())
            self.slug = to_assign
        super().save(*args, **kwargs)


class ListClient(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Lista de cliente'
        verbose_name_plural = 'Lista de clientes'
        ordering = ('-updated_at',)

    def __str__(self):
        return self.title


class ListItemClient(models.Model):
    list_client = models.ForeignKey(
        ListClient, on_delete=models.CASCADE, related_name='list_client')
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='client')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Item de lista de cliente'
        verbose_name_plural = 'ListItemClients'
        ordering = ('-updated_at',)

    def __str__(self):
        return self.list_client.title

    def get_count(self):
        return self.client.count()
