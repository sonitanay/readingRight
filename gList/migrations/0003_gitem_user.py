# Generated by Django 2.1.7 on 2021-06-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gList', '0002_auto_20210624_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='gitem',
            name='user',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
