from rest_framework import serializers

from account.serializers import UserSerializer
from forum.models import PostComment
from utils.api import ImageCode


class PostCommentSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source='create_user', read_only=True, needed_fields=['username', 'id', 'avatar'], avatar_base64=True)
    is_good = serializers.SerializerMethodField()
    reply_to_id = serializers.SerializerMethodField()
    reply_to_name = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = PostComment
        fields = [
            'id', 'user_info', 'is_good',
            'content', 'like_count', 'create_time',
            'reply_to_id', 'reply_to_name', 'under_comment_id',
            'comments_count',
            'create_time'
        ]

    def get_is_good(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.like_users.filter(id=request.user.id).exists()
        return False

    def get_reply_to_id(self, obj):
        return obj.reply_to_user.id if obj.reply_to_user else None

    def get_reply_to_name(self, obj):
        return obj.reply_to_user.username if obj.reply_to_user else None

    def get_comments_count(self, obj):
        return obj.secondary_comments.count()
