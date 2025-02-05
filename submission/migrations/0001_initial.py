# Generated by Django 5.1.2 on 2025-01-14 20:34

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.CharField(db_index=True, default=uuid.UUID('adef1d48-1f4f-40dc-997c-05491dad9267'), max_length=36, primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField(db_index=True)),
                ('code', models.TextField()),
                ('result', models.IntegerField(db_index=True, default=6)),
                ('time_spent', models.IntegerField(blank=True, null=True)),
                ('memory_spent', models.IntegerField(blank=True, null=True)),
                ('error_info', models.JSONField(null=True)),
                ('language', models.TextField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.problem')),
            ],
            options={
                'db_table': 'submission',
                'ordering': ('-create_time',),
            },
        ),
    ]
