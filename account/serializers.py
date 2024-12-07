from rest_framework import serializers

from account.models import User, Following


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

    class Meta:
        model = User
        fields = ['id', 'username', 'avatar', 'profile', 'subscribing_count', 'subscribers_count']

    def get_subscribing_count(self, obj):
        return obj.followings.count()

    def get_subscribers_count(self, obj):
        return obj.followers.count()


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