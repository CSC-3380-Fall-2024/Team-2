# Generated by Django 5.1.3 on 2024-12-10 03:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core_account", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                db_index=True,
                default="no-reply@example.com",
                max_length=254,
                unique=True,
            ),
        ),
    ]
