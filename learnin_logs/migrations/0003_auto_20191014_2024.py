# Generated by Django 2.2.6 on 2019-10-14 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learnin_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='data_added',
            new_name='date_added',
        ),
    ]
