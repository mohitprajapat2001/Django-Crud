# Generated by Django 4.1.3 on 2022-12-18 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='istrue',
            field=models.BooleanField(default=True),
        ),
    ]