# Generated by Django 5.0.2 on 2024-06-30 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_customuser_managers_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customuser',
            table='custom_user',
        ),
    ]