# Generated by Django 2.2.7 on 2019-11-26 20:05

from django.db import migrations, models
import ems.models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0007_auto_20191126_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='checkout',
            field=models.TimeField(default=ems.models.Visitor.get_default_my_time),
        ),
    ]