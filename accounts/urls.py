from django.urls import path
from . import views
from to_do.views import todo_view


urlpatterns = [
    path('register/', views.register , name='register') ,
    path('login/', views.login, name='login') ,
    path('logout/', views.logout, name='logout') ,
]