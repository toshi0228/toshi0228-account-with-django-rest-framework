# Generated by Django 2.2.2 on 2020-03-20 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200315_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='password',
            field=models.CharField(max_length=30, unique=True, verbose_name='password'),
        ),
    ]
