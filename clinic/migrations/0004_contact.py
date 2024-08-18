# Generated by Django 4.2.2 on 2024-08-18 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_carousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('opening_hours', models.CharField(max_length=100, verbose_name='Часы приема')),
                ('map', models.ImageField(blank=True, null=True, upload_to='contact/', verbose_name='Карта')),
            ],
        ),
    ]