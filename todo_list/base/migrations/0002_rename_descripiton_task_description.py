# Generated by Django 4.1.3 on 2023-02-25 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='descripiton',
            new_name='description',
        ),
    ]
