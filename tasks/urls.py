from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),         # 👈 Login is now the first page
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),           # 👈 Home (todo list) after login
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('finish/<int:task_id>/', views.finish_task, name='finish_task'),
]
