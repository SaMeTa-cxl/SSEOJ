from django.db import models

from account.models import User
from problem.models import Tag


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='create_posts')
    like_users = models.ManyToManyField(User, related_name='like_posts')
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(null=True)
    is_announcement = models.BooleanField(default=False)
    check_status = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, related_name='tags')

    class Meta:
        db_table = 'post'
        ordering = ('-last_update_time', '-create_time', )

    def __str__(self):
        return self.title


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='create_post_comments')
    like_users = models.ManyToManyField(User, related_name='like_post_comments')
    create_time = models.DateTimeField(auto_now_add=True)

    content = models.TextField()
    check_status = models.BooleanField(default=True)
    like_count = models.IntegerField(default=0)
    reply_to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reply_to_users', null=True, blank=True)
    under_comment_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='under_comments', null=True, blank=True)

    class Meta:
        db_table = 'post_comment'
        ordering = ('create_time',)

    def __str__(self):
        return '#' + str(self.id) + ':' + self.content[:20]
