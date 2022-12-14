# Generated by Django 3.2.5 on 2022-08-13 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campaign', '0007_rename_list_client_campaign_list_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_evaluation', models.CharField(choices=[('pendiente', 'Default'), ('positivo', 'Positive'), ('negativo', 'Negative'), ('no deseado', 'Not Wanted'), ('verificar número', 'Verify Number'), ('no aplica', 'Not Apply')], default='pendiente', max_length=50)),
                ('coment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_type_evaluation', to='campaign.contact')),
            ],
            options={
                'verbose_name': 'Evaluación',
                'verbose_name_plural': 'Evaaluaciones',
                'ordering': ('-updated_at',),
            },
        ),
    ]
