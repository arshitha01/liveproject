# Generated by Django 4.1.3 on 2023-03-17 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liveapp', '0007_rename_services_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
