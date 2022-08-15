from django.db import models
from django.template.defaultfilters import slugify

from apps.company.models import Company


class Contact(models.Model):

    class TypeContact(models.TextChoices):
        lead = 'nuevo contacto'
        client = 'cliente'

    type = models.CharField(
        max_length=50, choices=TypeContact.choices, default=TypeContact.lead)
    company = models.ForeignKey(
        Company, related_name='company_contact', on_delete=models.CASCADE)
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
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ('-updated_at',)

    def __str__(self):
        return self.name

    def get_fullname(self):
        return self.name + " " + self.lastname

    def save(self, *args, **kwargs):
        if not self.id:
            to_assign = slugify(self.name+self.lastname)
            if Contact.objects.filter(slug=to_assign).exists():
                to_assign = to_assign+str(Contact.objects.all().count())
            self.slug = to_assign
        super().save(*args, **kwargs)


class ListContact(models.Model):
    company = models.ForeignKey(
        Company, related_name='company_list_contact', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Lista de contacto'
        verbose_name_plural = 'Lista de contactos'
        ordering = ('-updated_at',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            to_assign = slugify(self.title)
            if ListContact.objects.filter(slug=to_assign).exists():
                to_assign = to_assign+str(ListContact.objects.all().count())
            self.slug = to_assign
        super().save(*args, **kwargs)


class ListItemContact(models.Model):
    list_contact = models.ForeignKey(
        ListContact, on_delete=models.CASCADE, related_name='list_contact')
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name='contact')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(
        Company, related_name='company_item_list', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'item de contacto '
        verbose_name_plural = 'items de contactos '
        ordering = ('-updated_at',)

    def __str__(self):
        return self.list_contact.title

    def get_count(self):
        return self.contact.count()


class Campaign(models.Model):
    company = models.ForeignKey(
        Company, related_name='company_campaigns', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    list_contact = models.ManyToManyField(
        ListContact, related_name='roster', blank=True)

    class Meta:
        verbose_name = 'Campaña'
        verbose_name_plural = 'Campañas'
        ordering = ('-updated_at',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            to_assign = slugify(self.title)
            if Campaign.objects.filter(slug=to_assign).exists():
                to_assign = to_assign+str(Campaign.objects.all().count())
            self.slug = to_assign
        super().save(*args, **kwargs)
