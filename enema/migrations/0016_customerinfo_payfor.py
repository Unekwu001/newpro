# Generated by Django 4.1.4 on 2023-01-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enema', '0015_roomates_pic1_roomates_pic2_roomates_pic3'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinfo',
            name='payfor',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
