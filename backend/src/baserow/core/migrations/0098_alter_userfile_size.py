# Generated by Django 5.0.13 on 2025-04-11 11:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0097_userprofile_completed_guided_tours"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userfile",
            name="size",
            field=models.PositiveBigIntegerField(),
        ),
    ]
