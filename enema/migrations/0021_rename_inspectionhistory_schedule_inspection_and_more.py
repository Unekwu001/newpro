# Generated by Django 4.1.4 on 2023-01-22 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enema', '0020_inspectionhistory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Inspectionhistory',
            new_name='Schedule_Inspection',
        ),
        migrations.AlterModelTable(
            name='schedule_inspection',
            table='schedule_inspection',
        ),
    ]
