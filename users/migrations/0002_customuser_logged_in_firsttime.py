# Generated by Django 3.1.7 on 2021-03-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='logged_in_firsttime',
            field=models.BooleanField(default=False, verbose_name='logged_in_firsttime'),
        ),
    ]
