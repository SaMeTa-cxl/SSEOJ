# Generated by Django 4.2.16 on 2025-01-12 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("problem", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="solutioncomment",
            name="under_comment_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="under_comments",
                to="problem.solutioncomment",
            ),
        ),
    ]