# Generated by Django 3.2.5 on 2022-08-10 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0003_listclient_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('list_client', models.ManyToManyField(blank=True, related_name='roster', to='campaign.ListClient')),
            ],
            options={
                'verbose_name': 'Campaña',
                'verbose_name_plural': 'Campañas',
                'ordering': ('-updated_at',),
            },
        ),
    ]
