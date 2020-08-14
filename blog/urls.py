from django.urls import path
from . import views

urlpatterns = [
    path('<year>/<chapternum>/', views.home, name='blog-home'),
    path('<year>/', views.index, name='blog-index'),
    path('', views.super, name='blog-super') 
    
]