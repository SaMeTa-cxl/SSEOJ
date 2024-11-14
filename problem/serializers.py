from rest_framework import serializers

from account.models import User
from problem.models import Problem, Solution, ProblemList


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        needed_fields = kwargs.pop('needed_fields', None)
        super(UserSerializer, self).__init__(*args, **kwargs)
        if needed_fields:
            for field in set(self.fields.keys()) - set(needed_fields):
                self.fields.pop(field)


class ProblemSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Problem
        exclude = ['star_users', 'pass_users', 'check_status']


class SolutionSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    user_info = UserSerializer(source='create_user', read_only=True, needed_fields=['id', 'username', 'avatar'])
    content = serializers.SerializerMethodField()

    class Meta:
        model = Solution
        exclude = ['like_users', 'check_status', 'problem', 'create_user']

    def get_content(self, obj):
        # 截断题解信息，减少一次性传递的数据量
        return obj.content[:200]


class ProblemListSerializer(serializers.ModelSerializer):
    creator = UserSerializer(source='create_user', read_only=True, needed_fields=['username'])

    class Meta:
        model = ProblemList
        fields = ['id', 'title', 'difficulty', 'problem_count', 'star_count', 'creator']

