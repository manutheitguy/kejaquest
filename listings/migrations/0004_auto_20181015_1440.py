# Generated by Django 2.1.1 on 2018-10-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20181015_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.IntegerField(),
        ),
    ]
