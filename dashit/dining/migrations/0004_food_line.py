# Generated by Django 3.1.2 on 2020-10-18 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dining', '0003_auto_20201018_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='line',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]