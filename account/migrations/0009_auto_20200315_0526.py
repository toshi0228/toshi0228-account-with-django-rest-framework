# Generated by Django 2.2.2 on 2020-03-15 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20200315_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(default=True, max_length=30, unique=True, verbose_name='ユーザー名'),
        ),
    ]