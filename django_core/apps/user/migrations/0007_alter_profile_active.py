# Generated by Django 5.0.6 on 2024-07-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_remove_customuser_bio_alter_profile_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="active",
            field=models.BooleanField(default=False),
        ),
    ]
