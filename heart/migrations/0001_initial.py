# Generated by Django 4.0.5 on 2022-06-06 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quartos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=100)),
                ('Data', models.DateField()),
                ('Noite', models.DecimalField(decimal_places=0, max_digits=3)),
                ('Imagem', models.FileField(upload_to='img_quarto/%d/%m/%y')),
                ('Tempo_quarto', models.IntegerField()),
                ('Nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
