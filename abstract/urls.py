from django.urls import path
from . import views

urlpatterns = [
    path('<year>/<chapternum>/', views.home, name='abstract-home'),
    path('<year>/', views.index, name='abstract-index'),
    path('', views.super, name='abstract-super')

]
