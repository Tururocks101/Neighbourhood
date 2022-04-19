from django.urls import path
from . import views

urlpatterns=[
    path('dashboard/',views.index, name='dashboard-index'),
    path('user/',views.user, name='dashboard-user'),
    path('business/',views.business, name='dashboard-business'),
    path('neighbourhood/',views.neighbourhood, name='dashboard-neighbourhood'),
]