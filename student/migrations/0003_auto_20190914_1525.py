# Generated by Django 2.2.5 on 2019-09-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190914_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(default='profile-2398782_960_720_ZjcWbXL.png', upload_to='images/'),
        ),
    ]
