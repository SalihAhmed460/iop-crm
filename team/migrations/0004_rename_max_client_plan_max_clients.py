# Generated by Django 5.0.3 on 2025-01-22 20:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("team", "0003_team_plan"),
    ]

    operations = [
        migrations.RenameField(
            model_name="plan",
            old_name="max_client",
            new_name="max_clients",
        ),
    ]
