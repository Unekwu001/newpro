# Generated by Django 4.1.4 on 2023-01-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enema', '0008_alter_agents_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomates',
            name='pic',
            field=models.FileField(blank=True, default='Null', null=True, upload_to='media/'),
        ),
    ]