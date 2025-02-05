# Generated by Django 5.1.2 on 2025-01-14 20:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('input_style', models.TextField()),
                ('output_style', models.TextField()),
                ('data_range', models.TextField(null=True)),
                ('sample', models.JSONField()),
                ('difficulty', models.IntegerField()),
                ('time_limit', models.IntegerField()),
                ('memory_limit', models.IntegerField()),
                ('pass_count', models.IntegerField(default=0)),
                ('attempt_count', models.IntegerField(default=0)),
                ('source', models.TextField(blank=True, null=True)),
                ('star_cnt', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('check_status', models.BooleanField(default=True)),
                ('test_case_id', models.TextField()),
                ('pass_users', models.ManyToManyField(related_name='pass_problems', to=settings.AUTH_USER_MODEL)),
                ('star_users', models.ManyToManyField(related_name='star_problems', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'problem',
                'ordering': ('create_time',),
            },
        ),
        migrations.CreateModel(
            name='ProblemList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('star_count', models.IntegerField(default=0)),
                ('problem_count', models.IntegerField(default=0)),
                ('summary', models.TextField(blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=False)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_problem_lists', to=settings.AUTH_USER_MODEL)),
                ('problems', models.ManyToManyField(related_name='problem_lists', to='problem.problem')),
                ('star_users', models.ManyToManyField(related_name='star_problem_lists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'problem_list',
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('title', models.TextField()),
                ('like_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('check_status', models.BooleanField(default=False)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_solutions', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(related_name='like_solutions', to=settings.AUTH_USER_MODEL)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='problem.problem')),
            ],
            options={
                'db_table': 'solution',
                'ordering': ('create_time',),
            },
        ),
        migrations.CreateModel(
            name='SolutionComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('like_count', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('check_status', models.BooleanField(default=False)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solution_comments', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(related_name='like_solution_comments', to=settings.AUTH_USER_MODEL)),
                ('reply_to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solution_comment_replies', to=settings.AUTH_USER_MODEL)),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='problem.solution')),
                ('under_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='under_comments', to='problem.solutioncomment')),
            ],
            options={
                'db_table': 'solution_comment',
                'ordering': ('create_time',),
            },
        ),
        migrations.CreateModel(
            name='StudyPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_time', models.DateTimeField(auto_now_add=True)),
                ('problem_status', models.BooleanField(default=False)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_plan', to='problem.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_plan', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'study_plan',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='problem.tag')),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.AddField(
            model_name='solution',
            name='tags',
            field=models.ManyToManyField(to='problem.tag'),
        ),
        migrations.AddField(
            model_name='problem',
            name='tags',
            field=models.ManyToManyField(to='problem.tag'),
        ),
    ]
