# Generated by Django 3.2.25 on 2024-04-24 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
