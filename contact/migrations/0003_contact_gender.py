# Generated by Django 4.1.5 on 2023-01-22 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='gender',
            field=models.CharField(default='askme', max_length=6),
            preserve_default=False,
        ),
    ]
