# Generated by Django 3.0.5 on 2020-05-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proServices', '0003_auto_20200520_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoeditingplans',
            name='type',
            field=models.CharField(choices=[('single', 'Single Job'), ('weekly', 'Weekly Plan'), ('monthly', 'Monthly Plan')], max_length=18),
        ),
    ]
