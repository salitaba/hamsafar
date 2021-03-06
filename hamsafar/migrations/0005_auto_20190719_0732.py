# Generated by Django 2.2 on 2019-07-19 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamsafar', '0004_requesttravel_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requesttravel',
            old_name='lat',
            new_name='end_lat',
        ),
        migrations.RenameField(
            model_name='requesttravel',
            old_name='long',
            new_name='end_long',
        ),
        migrations.AddField(
            model_name='requesttravel',
            name='start_lat',
            field=models.DecimalField(decimal_places=13, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requesttravel',
            name='start_long',
            field=models.DecimalField(decimal_places=13, default=1, max_digits=15),
            preserve_default=False,
        ),
    ]
