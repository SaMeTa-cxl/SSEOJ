from rest_framework import serializers

from account.models import User, Following
from problem.models import Problem, ProblemList, StudyPlan
from django.db.models import Q


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


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


class UserInfoSerializer(serializers.ModelSerializer):
    subscribing_count = serializers.SerializerMethodField()
    subscribers_count = serializers.SerializerMethodField()
    is_subscribe = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'avatar', 'profile', 'subscribing_count', 'subscribers_count']

    def get_subscribing_count(self, obj):
        return obj.followings.count()

    def get_subscribers_count(self, obj):
        return obj.followers.count()

    def get_is_subscribe(self, obj):
        user = self.context.get('user')

        if not user.is_authenticated:
            return True

        if user.id == obj.id:
            return True

        try:
            Following.objects.get(Q(follower = user) and Q(following = obj))
        except Following.DoesNotExist:
            return False

        return True


class UserFollowingSerializer(serializers.ModelSerializer):
    is_following_me = serializers.SerializerMethodField()
    is_followed_by_me = serializers.SerializerMethodField()
    is_mutual_following = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'profile']

    def get_is_following_me(self, obj):
        following_user = obj.following
        myself = self.context.get('myself')

        if myself:
            return Following.objects.get(follower=following_user, following=myself).exists()
        else:
            return False

    def get_is_followed_by_me(self, obj):
        following_user = obj.following
        myself = self.context.get('myself')

        if myself:
            return Following.objects.get(follower=myself, following=following_user).exists()
        else:
            return False

    def get_is_mutual_following(self, obj):
        following_user = obj.following
        myself = self.context.get('myself')

        if self.is_following_me and self.is_followed_by_me:
            return True
        else:
            return False


class UserLogInformation(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'avatar', 'user_type')


class GetStudyPlanSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    difficulty = serializers.SerializerMethodField()

    class Meta:
        model = StudyPlan
        fields = ['problem_status']

    def get_id(self, obj):
        return obj.problem.idw

    def get_name(self, obj):
        return obj.problem.name

    def get_difficulty(self, obj):
        return obj.problem.difficulty


class ProblemListSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = ProblemList
        fields = ('id', 'title', 'problem_count', 'type')

    def get_type(self, obj):
        return obj.is_public
