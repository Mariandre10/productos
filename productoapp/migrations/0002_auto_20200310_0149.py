# Generated by Django 2.2.11 on 2020-03-10 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
