# Generated by Django 5.0.3 on 2025-01-22 19:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lead", "0005_lead_team"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="lead",
            options={"ordering": ("name",)},
        ),
    ]
