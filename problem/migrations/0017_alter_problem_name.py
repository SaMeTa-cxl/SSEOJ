# Generated by Django 5.1.2 on 2025-01-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0016_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
