# Generated by Django 4.1.4 on 2023-01-12 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0004_alter_products_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Figures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
        ),
    ]
