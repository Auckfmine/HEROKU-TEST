# Generated by Django 2.2.5 on 2019-10-01 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement',
            name='valid_until',
            field=models.DateField(default=datetime.date(2019, 11, 1), verbose_name='valid until'),
        ),
    ]
