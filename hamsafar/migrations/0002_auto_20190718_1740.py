# Generated by Django 2.2 on 2019-07-18 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hamsafar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='profile',
            new_name='user',
        ),
    ]
