# Generated by Django 4.1.5 on 2023-01-15 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
