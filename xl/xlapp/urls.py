from django.urls import path, include
from xlapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('a/', views.xl, name='xl'),
    path('show/', views.show, name='show'),
]