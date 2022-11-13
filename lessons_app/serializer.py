from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from django.contrib.auth.models import User

from .models import Lesson, UserDetail, TimeBlock


class LessonSerializer(serializers.ModelSerializer):

    # student = PrimaryKeyRelatedField(read_only=True)
    # salary = serializers.IntegerField(read_only=True)

    class Meta:
        model = Lesson
        fields = ('id', 'student', 'salary', 'time', 'date')


class RegistrationSerializer(serializers.Serializer):
    """ Registraion new user (allow any) """

    username = serializers.CharField()
    first_name = serializers.CharField()
    password = serializers.CharField()
    phone = serializers.CharField(allow_blank=True, required=False, default='')
    telegram = serializers.CharField(allow_blank=True, required=False, default='')
    last_login = serializers.DateTimeField()
    date_joined = serializers.DateTimeField()


class BlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeBlock
        fields = ('id', 'date', 'start_time', 'end_time')
