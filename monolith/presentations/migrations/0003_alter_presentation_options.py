# Generated by Django 4.0.3 on 2023-03-23 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0002_alter_presentation_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='presentation',
            options={'ordering': ('title',)},
        ),
    ]
