# Generated by Django 5.0.3 on 2025-01-20 03:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lead", "0002_rename_desrcipton_lead_desrciption"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lead",
            old_name="desrciption",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="lead",
            old_name="priory",
            new_name="priority",
        ),
    ]
