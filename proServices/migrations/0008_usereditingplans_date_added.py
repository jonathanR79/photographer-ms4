# Generated by Django 3.0.5 on 2020-05-23 11:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('proServices', '0007_auto_20200520_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='usereditingplans',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]