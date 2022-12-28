from django.urls import path, re_path
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('app/<int:pk>/', views.IndexView.as_view(), name='new'),
]

