from rest_framework import serializers

from account.models import User


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
