# Generated by Django 4.1.5 on 2023-01-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
    ]
