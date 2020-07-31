from django.urls import path
from . import views
from to_do.views import todo_view


urlpatterns = [
    path('todo/', views.todo_view , name='todo_view') ,
  
    path("deleteTodo/<int:todo_id>/", views.delete_todo, name='delete_todo'),
    path('update_todo/<str:pk>/', views.update_todo , name='update_todo') ,
]


