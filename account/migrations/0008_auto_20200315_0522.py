# Generated by Django 2.2.2 on 2020-03-15 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_myuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(default=True, max_length=30, verbose_name='ユーザー名'),
        ),
    ]
