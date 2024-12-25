# Generated by Django 5.1.2 on 2024-12-19 03:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0003_alter_submission_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='info',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='shared',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='statistic_info',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='username',
        ),
        migrations.AddField(
            model_name='submission',
            name='error_info',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='memory_spent',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='time_spent',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submission',
            name='id',
            field=models.CharField(db_index=True, default=uuid.UUID('47b247ba-91b9-44b6-b6ad-e5d61dc31e3e'), max_length=36, primary_key=True, serialize=False),
        ),
    ]
