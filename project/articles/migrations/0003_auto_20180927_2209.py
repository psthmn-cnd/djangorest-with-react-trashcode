# Generated by Django 2.1.1 on 2018-09-27 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20180927_2209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='heade_pl',
            new_name='header_pl',
        ),
    ]
