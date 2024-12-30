# Generated by Django 4.2.16 on 2024-12-30 13:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("submission", "0006_alter_submission_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submission",
            name="id",
            field=models.CharField(
                db_index=True,
                default=uuid.UUID("e975a70f-40ce-448e-a0ec-a70ae9910125"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
