# Generated by Django 4.1.4 on 2023-01-11 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enema', '0012_alter_customerinfo_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='phonenumber',
            field=models.CharField(max_length=150),
        ),
    ]
