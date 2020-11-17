# Generated by Django 2.1.4 on 2020-11-16 18:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ur', '0012_auto_20181220_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='urfiles', verbose_name='Zdjęcie'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='add_date',
            field=models.DateField(default=datetime.date(2020, 11, 16), verbose_name='Data dodania'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='expiry_date',
            field=models.DateField(default=datetime.date(2020, 11, 16), verbose_name='Do kiedy wkonac zlecenie'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='fix_date',
            field=models.DateField(blank=True, default=datetime.date(2020, 11, 16), verbose_name='Data usunięcia usterki'),
        ),
    ]