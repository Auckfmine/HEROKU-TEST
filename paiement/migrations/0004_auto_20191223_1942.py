# Generated by Django 2.2.5 on 2019-12-23 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0003_auto_20191106_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement',
            name='valid_until',
            field=models.DateField(verbose_name='valid until'),
        ),
    ]
