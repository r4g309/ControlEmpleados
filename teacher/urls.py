from django.urls import path

from .views import HomeView, ListTeacherView, CreateTeacherView, ShowInfo, ShowAllTeachers

app_name = "teacher"
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('list/', ListTeacherView.as_view(), name="list_teacher"),
    path('create/', CreateTeacherView.as_view(), name="create_teacher"),
    path('show_info/<int:id_user>/', ShowInfo.as_view(), name="show_info"),
    path('show_all/', ShowAllTeachers.as_view(), name="show_all")

]
