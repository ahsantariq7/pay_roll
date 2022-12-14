# Generated by Django 4.0.6 on 2022-08-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_accountant',
            field=models.BooleanField(default=False, verbose_name='Accountant Account Type'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_business',
            field=models.BooleanField(default=False, verbose_name='Business/Company(Business Account Type)'),
        ),
    ]
