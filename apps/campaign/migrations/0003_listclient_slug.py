# Generated by Django 3.2.5 on 2022-08-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_auto_20220809_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='listclient',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
