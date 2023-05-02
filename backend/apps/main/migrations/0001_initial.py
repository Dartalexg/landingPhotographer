# Generated by Django 4.2 on 2023-04-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zapis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон')),
                ('date', models.DateTimeField(null=True, verbose_name='Дата записиси')),
                ('type_photoset', models.IntegerField(blank=True, choices=[(0, 'Индивидуальная'), (1, 'Семейная'), (2, 'Парная'), (3, 'Видеоролики с фото'), (4, 'Детская'), (5, 'Мероприятия'), (6, 'Животные'), (7, 'Коллаж')], null=True, verbose_name='Тип фотосессии')),
            ],
            options={
                'verbose_name': 'Запись на фото',
                'verbose_name_plural': 'Запись на фото',
            },
        ),
    ]