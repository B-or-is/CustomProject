# Generated by Django 4.0.4 on 2022-05-05 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='brand_name',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='custom_admin.brand'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='custom_admin.category'),
        ),
    ]