# Generated by Django 4.2.17 on 2024-12-12 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email_address',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
