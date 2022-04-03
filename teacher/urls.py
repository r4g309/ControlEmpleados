from django.urls import path
from .views import HomeView,ListTeacherView

app_name="teacher"
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('list/',ListTeacherView.as_view(),name="list_teacher")

]
