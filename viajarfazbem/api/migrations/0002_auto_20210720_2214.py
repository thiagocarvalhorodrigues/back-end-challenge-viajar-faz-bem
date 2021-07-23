# Generated by Django 3.2.5 on 2021-07-21 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vitrine',
            name='item',
            field=models.ManyToManyField(related_name='item', to='api.Item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='api.category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='city',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city', to='api.city'),
        ),
        migrations.AlterField(
            model_name='item',
            name='country',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country', to='api.country'),
        ),
        migrations.AlterField(
            model_name='vitrine',
            name='routes',
            field=models.ManyToManyField(related_name='routes', to='api.Routers'),
        ),
    ]