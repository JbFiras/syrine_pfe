# Generated by Django 3.2.7 on 2022-06-09 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('mes', '0007_rename_limite_objectif_production_objectif'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produced_Product_Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectif', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('equipe', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipe_produced_number', to='accounts.equipe')),
            ],
        ),
    ]