# Generated by Django 5.1.2 on 2025-01-14 20:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('like_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(null=True)),
                ('is_announcement', models.BooleanField(default=False)),
                ('check_status', models.BooleanField(default=True)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_posts', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(related_name='tags', to='problem.tag')),
            ],
            options={
                'db_table': 'post',
                'ordering': ('-last_update_time', '-create_time'),
            },
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('check_status', models.BooleanField(default=True)),
                ('like_count', models.IntegerField(default=0)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_post_comments', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(related_name='like_post_comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.post')),
                ('reply_to_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_to_users', to=settings.AUTH_USER_MODEL)),
                ('under_comment_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_comments', to='forum.postcomment')),
            ],
            options={
                'db_table': 'post_comment',
                'ordering': ('create_time',),
            },
        ),
    ]
