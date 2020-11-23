# Generated by Django 2.1.4 on 2020-11-20 21:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ur', '0002_auto_20201118_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='add_date',
            field=models.DateField(default=datetime.date(2020, 11, 20), verbose_name='Data dodania'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='expiry_date',
            field=models.DateField(default=datetime.date(2020, 11, 20), verbose_name='Do kiedy wkonac zlecenie'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='fix_date',
            field=models.DateField(blank=True, default=datetime.date(2020, 11, 20), verbose_name='Data usunięcia usterki'),
        ),
    ]
