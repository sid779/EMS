# Generated by Django 2.2.7 on 2019-11-24 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0002_auto_20191123_2301'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Visitor',
        ),
        migrations.RenameField(
            model_name='visitor',
            old_name='user_name',
            new_name='visitor_name',
        ),
    ]
