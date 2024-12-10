from rest_framework import serializers

from account.models import User
from account.serializers import UserSerializer
from problem.models import Problem, Solution, ProblemList, Tag


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


class SolutionSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source='create_user', read_only=True, needed_fields=['id', 'username', 'avatar'])

    class Meta:
        model = Solution
        exclude = ['like_users', 'check_status', 'problem', 'create_user']


class ProblemListSerializer(serializers.ModelSerializer):
    creator = UserSerializer(source='create_user', read_only=True, needed_fields=['username'])

    class Meta:
        model = ProblemList
        fields = ['id', 'title', 'difficulty', 'problem_count', 'star_count', 'creator']


class ProblemListDetailSerializer(serializers.ModelSerializer):
    creator_info = UserSerializer(source='create_user', read_only=True, needed_fields=['id', 'username'])
    problems = ProblemSerializer(many=True, read_only=True, needed_fields=['id', 'name', 'difficulty',
                                                                           'tags', 'pass_count', 'attempt_count'])

    class Meta:
        model = ProblemList
        fields = ['id', 'title', 'summary', 'creator_info', 'problems']


class SolutionCreateSerializer(serializers.Serializer):
    problem_id = serializers.IntegerField()
    content = serializers.CharField()
    tags = serializers.ListField(child=serializers.IntegerField(), allow_null=True, required=False)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
