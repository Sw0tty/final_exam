# Generated by Django 4.2.6 on 2023-10-27 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism_app', '0004_alter_mountaincoords_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountainlevel',
            name='autumn',
            field=models.CharField(choices=[('B', 'Теплая одеждка будет кстате'), ('A', 'Приятная прогулка'), ('D', 'Невыносимое испытание'), ('C', 'Лучше идти группой'), (None, 'Выберите сложность')], max_length=2),
        ),
        migrations.AlterField(
            model_name='mountainlevel',
            name='spring',
            field=models.CharField(choices=[('B', 'Теплая одеждка будет кстате'), ('A', 'Приятная прогулка'), ('D', 'Невыносимое испытание'), ('C', 'Лучше идти группой'), (None, 'Выберите сложность')], max_length=2),
        ),
        migrations.AlterField(
            model_name='mountainlevel',
            name='summer',
            field=models.CharField(choices=[('B', 'Теплая одеждка будет кстате'), ('A', 'Приятная прогулка'), ('D', 'Невыносимое испытание'), ('C', 'Лучше идти группой'), (None, 'Выберите сложность')], max_length=2),
        ),
        migrations.AlterField(
            model_name='mountainlevel',
            name='winter',
            field=models.CharField(choices=[('B', 'Теплая одеждка будет кстате'), ('A', 'Приятная прогулка'), ('D', 'Невыносимое испытание'), ('C', 'Лучше идти группой'), (None, 'Выберите сложность')], max_length=2),
        ),
        migrations.AlterField(
            model_name='mountainpass',
            name='status',
            field=models.CharField(choices=[('pending', 'Проводится модерация'), ('new', 'Новая запись'), ('accepted', 'Запись опубликована'), ('rejected', 'Запись отклонена')], default='new', max_length=8),
        ),
    ]