# Generated by Django 4.0.5 on 2022-06-06 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0002_alugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='alugar',
            name='Vago',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]