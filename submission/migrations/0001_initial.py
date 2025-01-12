# Generated by Django 4.2.16 on 2025-01-12 15:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("problem", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Submission",
            fields=[
                (
                    "id",
                    models.CharField(
                        db_index=True,
                        default=uuid.UUID("f06f08a0-53ed-4af7-b222-94e3134daa2a"),
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                ("user_id", models.IntegerField(db_index=True)),
                ("code", models.TextField()),
                ("result", models.IntegerField(db_index=True, default=6)),
                ("time_spent", models.IntegerField(blank=True, null=True)),
                ("memory_spent", models.IntegerField(blank=True, null=True)),
                ("error_info", models.JSONField(null=True)),
                ("language", models.TextField()),
                (
                    "problem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="problem.problem",
                    ),
                ),
            ],
            options={
                "db_table": "submission",
                "ordering": ("-create_time",),
            },
        ),
    ]
