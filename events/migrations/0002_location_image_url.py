# Generated by Django 4.0.3 on 2023-03-23 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image_url',
            field=models.CharField(default='none', max_length=200),
        ),
    ]