# Generated by Django 4.1.4 on 2022-12-30 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Null', max_length=100)),
                ('email', models.CharField(default='Null', max_length=100, unique=True)),
                ('pwd', models.CharField(default='Null', max_length=100)),
                ('phone', models.CharField(default='Null', max_length=15)),
                ('address', models.CharField(default='Null', max_length=230)),
                ('id_type', models.CharField(default='Null', max_length=30)),
                ('id_numb', models.CharField(default='Null', max_length=30)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('points', models.CharField(default='Null', max_length=15)),
            ],
            options={
                'db_table': 'agents',
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default='Null', max_length=100)),
                ('school', models.CharField(default='Null', max_length=30)),
            ],
            options={
                'db_table': 'locations',
            },
        ),
        migrations.CreateModel(
            name='Lodges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Null', max_length=50)),
                ('location', models.CharField(default='Null', max_length=100)),
                ('lodgetype', models.CharField(default='Null', max_length=30)),
                ('price', models.CharField(default='Null', max_length=15)),
                ('Tiled', models.CharField(default='Null', max_length=15)),
                ('light', models.CharField(default='Null', max_length=15)),
                ('water', models.CharField(default='Null', max_length=15)),
                ('status', models.CharField(default='Null', max_length=15)),
                ('region', models.CharField(default='Null', max_length=15)),
                ('agentid', models.CharField(default='Null', max_length=15)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'lodges',
            },
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'schools',
            },
        ),
        migrations.CreateModel(
            name='Lodgepics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picname', models.CharField(blank=True, max_length=100, null=True)),
                ('agentid', models.CharField(default='Null', max_length=15)),
                ('sn', models.IntegerField(blank=True, null=True)),
                ('lodgeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enema.lodges')),
            ],
            options={
                'db_table': 'lodgepics',
            },
        ),
    ]
