# Generated by Django 4.1.3 on 2023-03-16 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liveapp', '0004_rename_message_contact_usermessage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
