# Generated by Django 4.1.4 on 2023-01-12 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0003_rename_categotia_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.BooleanField(default=True),
        ),
    ]