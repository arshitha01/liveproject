# Generated by Django 4.1.3 on 2023-03-17 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liveapp', '0005_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='service',
            new_name='servicename',
        ),
    ]