# Generated by Django 2.1.1 on 2018-10-15 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20181012_1425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='garage',
            new_name='parking',
        ),
    ]
