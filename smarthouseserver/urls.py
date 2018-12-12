from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('status/', views.status, name='status'),
    path('status/<int:pin>/', views.status, name='status'),

    path('on/<int:pin>/', views.on, name='on'),
    path('off/<int:pin>/', views.off, name='off'),

]
