# Generated by Django 3.2.25 on 2024-05-03 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0010_customuser'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customuser',
            unique_together={('username',)},
        ),
    ]
