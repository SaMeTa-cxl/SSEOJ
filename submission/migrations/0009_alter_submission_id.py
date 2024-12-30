# Generated by Django 4.2.16 on 2024-12-30 14:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("submission", "0008_alter_submission_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submission",
            name="id",
            field=models.CharField(
                db_index=True,
                default=uuid.UUID("4831e081-8fd7-4636-9eef-67bcf19ceb1e"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
