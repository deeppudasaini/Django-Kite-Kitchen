# Generated by Django 2.2.13 on 2021-06-16 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_updates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updates',
            name='updateDescription',
            field=models.CharField(max_length=150),
        ),
    ]
