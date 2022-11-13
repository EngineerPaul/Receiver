from django.urls import path

from .views import Homepage, AddUserAPI, AddLessonAPI, AddBlockAPI


urlpatterns = [
    path('', Homepage.as_view()),
    path('api/add_user', AddUserAPI.as_view()),
    path('api/add_lesson', AddLessonAPI.as_view()),
    path('api/add_block', AddBlockAPI.as_view())
]
