from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<ec>', views.index, name='index'),
    path('record/', views.record, name='record'),
]