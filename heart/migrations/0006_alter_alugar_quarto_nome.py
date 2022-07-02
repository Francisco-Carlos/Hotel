# Generated by Django 4.0.5 on 2022-06-08 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('heart', '0005_alugar_quarto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alugar_quarto',
            name='Nome',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]