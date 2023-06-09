# Generated by Django 4.2.1 on 2023-05-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=66, verbose_name='Название товара')),
                ('country', models.CharField(max_length=60, verbose_name='Страна производитель')),
                ('impact', models.CharField(max_length=255, verbose_name='Воздействие')),
                ('taste', models.CharField(max_length=255, verbose_name='Вкус')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
            ],
        ),
    ]
