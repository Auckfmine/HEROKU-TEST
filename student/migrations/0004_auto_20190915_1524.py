# Generated by Django 2.2.5 on 2019-09-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20190914_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(default='/images/profile.png', upload_to='images/'),
        ),
    ]
