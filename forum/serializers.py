from rest_framework import serializers

from forum.models import PostComment
from utils.api import ImageCode


class PostCommentSerializer(serializers.ModelSerializer):
    comment_id = serializers.IntegerField(source='id')
    user_id = serializers.IntegerField(source='create_user.id')
    user_name = serializers.CharField(source='create_user.username')
    comment_content = serializers.CharField(source='content')
    avatar = serializers.SerializerMethodField()
    like_status = serializers.SerializerMethodField()
    reply_to_id = serializers.SerializerMethodField()
    reply_to_name = serializers.SerializerMethodField()

    class Meta:
        model = PostComment
        fields = [
            'comment_id', 'user_id', 'user_name', 'avatar', 'like_status',
            'comment_content', 'like_count', 'create_time',
            'reply_to_id', 'reply_to_name', 'under_comment_id'
        ]

    def get_avatar(self, obj):
        return str(ImageCode.image_base64(obj.create_user.avatar))

    def get_like_status(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.like_users.filter(id=request.user.id).exists()
        return False

    def get_reply_to_id(self, obj):
        return obj.reply_to_user.id if obj.reply_to_user else None

    def get_reply_to_name(self, obj):
        return obj.reply_to_user.username if obj.reply_to_user else None
