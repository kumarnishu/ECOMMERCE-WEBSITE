# Generated by Django 3.0.3 on 2020-02-20 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_contacts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='fistname',
            new_name='firstname',
        ),
    ]
