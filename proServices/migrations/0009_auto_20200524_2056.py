# Generated by Django 3.0.5 on 2020-05-24 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proServices', '0008_usereditingplans_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usereditingplans',
            name='date_added',
            field=models.DateTimeField(),
        ),
    ]
