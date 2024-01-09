from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('register/', views.Register, name='register'),
    path('login/', views.UserLogin, name='login'),
    path('logout/', views.UserLogOut, name='logout'),
    path('header/', views.Header, name='header'),
    path('addtask/', views.AddTask, name='addtask'),
    path('tasks/', views.Tasks, name='tasks'),
    path('completedtask/<int:task_id>/', views.DeleteTask, name='completedtask'),
    path('edittask/<int:task_id>/', views.EditTask, name='edittask'),
]
