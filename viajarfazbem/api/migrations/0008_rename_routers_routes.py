# Generated by Django 3.2.5 on 2021-07-22 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_item_city'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Routers',
            new_name='Routes',
        ),
    ]
