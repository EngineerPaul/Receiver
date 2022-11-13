from copy import deepcopy

from django.views.generic import TemplateView
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .models import Lesson, UserDetail, TimeBlock
from .serializer import (
    LessonSerializer, RegistrationSerializer, BlockSerializer
)


class Homepage(TemplateView):
    template_name = 'lessons_app/index.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['len_users'] = len(context['users'])
        context['lessons'] = Lesson.objects.all()
        context['len_lessons'] = len(context['lessons'])
        context['blocks'] = TimeBlock.objects.all()
        context['len_blocks'] = len(context['blocks'])
        return context


class AddLessonAPI(CreateAPIView):

    serializer_class = LessonSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # print('CreateAPIView: ', request)
        # print('11111111111111111111111111111111111111111111111111')
        return self.create(request, *args, **kwargs)


class AddUserAPI(CreateAPIView):

    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # print('CreateAPIView: ', request)
        # print('11111111111111111111111111111111111111111111111111')
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User()
        userdetail = UserDetail()

        user.username = serializer.data['username']
        # password already hashed
        # user.password = make_password(serializer.data['password'])
        user.password = serializer.data['password']
        user.first_name = serializer.data['first_name']

        userdetail.user = user
        userdetail.phone = serializer.data['phone']
        userdetail.telegram = serializer.data['telegram']

        user.last_login = serializer.data['last_login']
        user.date_joined = serializer.data['date_joined']

        user.save()
        userdetail.save()

        obj = deepcopy(serializer.data)
        obj['id'] = user.id

        headers = self.get_success_headers(serializer.data)
        return Response(
            obj,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class AddBlockAPI(CreateAPIView):

    serializer_class = BlockSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # print('CreateAPIView: ', request)
        # print('11111111111111111111111111111111111111111111111111')
        return self.create(request, *args, **kwargs)
