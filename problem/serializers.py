from rest_framework import serializers

from account.models import User
from account.serializers import UserSerializer
from problem.models import Problem, Solution, ProblemList, Tag, SolutionComment


class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        exclude = ['star_users', 'pass_users', 'check_status', 'create_time']

    def __init__(self, *args, **kwargs):
        needed_fields = kwargs.pop('needed_fields', None)
        super(ProblemSerializer, self).__init__(*args, **kwargs)
        if needed_fields:
            for field in set(self.fields.keys()) - set(needed_fields):
                self.fields.pop(field)


class ProblemCreateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    input_style = serializers.CharField()
    output_style = serializers.CharField()
    data_range = serializers.CharField(required=False)
    difficulty = serializers.IntegerField
    time_limit = serializers.IntegerField()
    memory_limit = serializers.IntegerField()
    samples = serializers.JSONField()
    tags = serializers.JSONField()
    source = serializers.CharField(required=False)



class SolutionSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source='create_user', read_only=True, needed_fields=['id', 'username', 'avatar'])

    class Meta:
        model = Solution
        exclude = ['like_users', 'check_status', 'problem', 'create_user']


class ProblemListSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source='create_user', read_only=True, needed_fields=['username', 'avatar'])

    class Meta:
        model = ProblemList
        fields = ['id', 'title', 'problem_count', 'star_count', 'user_info']


class ProblemListDetailSerializer(serializers.ModelSerializer):
    creator_info = UserSerializer(source='create_user', read_only=True, needed_fields=['id', 'username'])
    problems = ProblemSerializer(many=True, read_only=True, needed_fields=['id', 'name', 'difficulty',
                                                                           'tags', 'pass_count', 'attempt_count'])
    name = serializers.CharField(source='title', read_only=True)

    class Meta:
        model = ProblemList
        fields = ['id', 'name', 'summary', 'creator_info', 'problems', 'problem_count']


class SolutionCreateSerializer(serializers.Serializer):
    problem_id = serializers.IntegerField()
    content = serializers.CharField()
    tags = serializers.ListField(child=serializers.IntegerField(), allow_null=True, required=False)


class ProblemListCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    summary = serializers.CharField()
    type = serializers.BooleanField()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class SolutionCommentSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source='create_user', read_only=True, needed_fields=['id', 'username', 'avatar'])
    reply_to_user_info = UserSerializer(source='reply_to_user', read_only=True, needed_fields=['id', 'username'])

    class Meta:
        model = SolutionComment
        fields = ['id', 'user_info', 'content', 'like_count', 'create_time', 'reply_to_user_info']
