from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('earn', views.earn, name="earn"),
    path('friends', views.friends, name="friends"),
]
