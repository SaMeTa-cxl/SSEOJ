# Generated by Django 5.1.2 on 2024-12-30 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0015_alter_tag_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
