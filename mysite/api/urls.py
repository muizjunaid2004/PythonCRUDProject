from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.overview, name = 'overview'),
    path('task-list/', views.taskList, name = 'list' ),
    path('task-detail/<str:pk>/', views.taskDetail, name = 'detail'),
    path('task-create/', views.taskCreate, name = 'create'),
    path('task-update/<str:pk>', views.taskUpdate, name = 'update'),
    path('task-delete/<str:pk>', views.taskUpdate, name = 'update')
]
