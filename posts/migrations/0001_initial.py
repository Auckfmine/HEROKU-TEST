# Generated by Django 3.1.1 on 2020-09-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=120, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('section', models.CharField(choices=[('petit-section', 'Petit-Section'), ('moyenne-section', 'Moyenne-Section'), ('grand-section', 'Grand-Section')], max_length=25)),
            ],
        ),
    ]