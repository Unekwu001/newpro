# Generated by Django 4.1.4 on 2023-01-21 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enema', '0018_agents_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='agents',
            name='status',
            field=models.CharField(blank=True, default='unverified', max_length=15, null=True),
        ),
    ]