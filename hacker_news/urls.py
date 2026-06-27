from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='new_list')
]