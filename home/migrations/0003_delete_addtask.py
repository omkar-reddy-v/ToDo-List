# Generated by Django 5.0.3 on 2024-03-27 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_addtask_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='addtask',
        ),
    ]