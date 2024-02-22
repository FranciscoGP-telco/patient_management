from django.urls import path
from . import views

urlpatterns = [
    path('commoninfo/add', views.add, name='add'),
    path('commoninfo/fetch', views.fetch, name='fetch'),
]
