from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_page, name='default_page'),
    path('search', views.default_page, name='default_page')
]
