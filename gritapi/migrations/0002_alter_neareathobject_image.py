# Generated by Django 3.2.4 on 2021-06-18 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gritapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neareathobject',
            name='image',
            field=models.CharField(max_length=250),
        ),
    ]