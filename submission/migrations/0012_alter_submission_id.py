# Generated by Django 5.1.2 on 2025-01-02 14:28

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0011_alter_submission_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='id',
            field=models.CharField(db_index=True, default=uuid.UUID('ca5d74a6-cf7a-4c4e-8bf9-6b6484ca444d'), max_length=36, primary_key=True, serialize=False),
        ),
    ]