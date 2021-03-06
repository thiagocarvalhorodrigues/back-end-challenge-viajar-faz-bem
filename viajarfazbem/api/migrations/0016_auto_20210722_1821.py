# Generated by Django 3.2.5 on 2021-07-22 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20210722_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='api.category'),
        ),
        migrations.RemoveField(
            model_name='item',
            name='country',
        ),
        migrations.AddField(
            model_name='item',
            name='country',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country', to='api.country'),
        ),
    ]
