# Generated by Django 4.2.6 on 2023-10-27 09:22

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
            name='Tourist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('otc', models.CharField(max_length=255)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MountainPass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('other_titles', models.CharField(max_length=255)),
                ('connect', models.CharField(max_length=255)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('person_add', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='person_add', to='tourism_app.tourist')),
            ],
        ),
        migrations.CreateModel(
            name='MountainLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summer', models.CharField(choices=[('A', 'Приятная прогулка'), ('D', 'Невыносимое испытание'), ('B', 'Теплая одеждка будет кстате'), ('C', 'Лучше идти группой')], max_length=2)),
                ('autumn', models.CharField(choices=[('A', 'Приятная прогулка'), ('D', 'Невыносимое испытание'), ('B', 'Теплая одеждка будет кстате'), ('C', 'Лучше идти группой')], max_length=2)),
                ('spring', models.CharField(choices=[('A', 'Приятная прогулка'), ('D', 'Невыносимое испытание'), ('B', 'Теплая одеждка будет кстате'), ('C', 'Лучше идти группой')], max_length=2)),
                ('winter', models.CharField(choices=[('A', 'Приятная прогулка'), ('D', 'Невыносимое испытание'), ('B', 'Теплая одеждка будет кстате'), ('C', 'Лучше идти группой')], max_length=2)),
                ('hard_level', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tourism_app.mountainpass')),
            ],
        ),
        migrations.CreateModel(
            name='MountainCoords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
                ('height', models.FloatField()),
                ('mountain_pass', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tourism_app.mountainpass')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('mountain_image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tourism_app.mountainpass')),
            ],
        ),
    ]
