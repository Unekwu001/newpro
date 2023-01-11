# Generated by Django 4.1.4 on 2023-01-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enema', '0010_customerinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerinfo',
            old_name='firstname',
            new_name='fullname',
        ),
        migrations.RemoveField(
            model_name='customerinfo',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='customerinfo',
            name='state',
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='phonenumber',
            field=models.IntegerField(max_length=20),
        ),
    ]