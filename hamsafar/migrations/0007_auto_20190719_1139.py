# Generated by Django 2.2 on 2019-07-19 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hamsafar', '0006_auto_20190719_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requesttravel',
            old_name='end_city',
            new_name='end_road',
        ),
        migrations.RenameField(
            model_name='requesttravel',
            old_name='start_city',
            new_name='start_road',
        ),
    ]
