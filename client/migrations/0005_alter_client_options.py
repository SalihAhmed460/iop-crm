# Generated by Django 5.0.3 on 2025-01-22 19:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("client", "0004_client_team"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={"ordering": ("name",)},
        ),
    ]
