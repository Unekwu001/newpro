# Generated by Django 4.1.4 on 2023-02-01 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enema', '0028_hosting_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hosting_table',
            new_name='Hosts',
        ),
    ]
