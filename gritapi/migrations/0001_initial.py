# Generated by Django 3.2.4 on 2021-06-11 14:27

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
            name='NearEathObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neo_reference', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('estimated_diameter', models.IntegerField()),
                ('is_potentially_hazardous', models.BooleanField()),
                ('close_approach_date', models.DateField()),
                ('miles_per_hour', models.CharField(max_length=50)),
                ('orbiting_body', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gritapi.neareathobject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]