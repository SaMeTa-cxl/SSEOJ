from rest_framework import serializers

from account.models import User
from problem.models import Problem, Solution


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'avatar']


class ProblemSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Problem
        exclude = ['star_users', 'pass_users', 'check_status']


class SolutionSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    user_info = UserSerializer(source='create_user', read_only=True)
    content = serializers.SerializerMethodField()

    class Meta:
        model = Solution
        exclude = ['like_users', 'check_status', 'problem', 'create_user']

    def get_content(self, obj):
        return obj.content[:200]
