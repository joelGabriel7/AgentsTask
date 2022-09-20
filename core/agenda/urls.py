from django.urls import path
from core.agenda.views import *
urlpatterns = [
    path('task/list/', TaskList.as_view(), name='task_list'),
    path('task/add/', TaskCreateView.as_view(), name='task_create'),
    path('task/edit/<int:pk>/', TaskUpdateView.as_view(), name='task_edit'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
]