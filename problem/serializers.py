from rest_framework import serializers

from problem.models import Problem


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        exclude = ['star_users', 'pass_users']


# class SimilarProblemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Problem

