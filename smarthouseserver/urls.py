from django.urls import path, include
from . import controls

urlpatterns = [
    path('', controls.index, name='index'),

    path('status/', controls.status, name='status'),
    path('status/<int:pin>/', controls.status, name='status'),

    path('on/<int:pin>/', controls.on, name='on'),
    path('off/<int:pin>/', controls.off, name='off'),

]
