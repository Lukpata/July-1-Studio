from django.urls import path
from .import views

urlpatterns = [
    path('', views.News_page, name='news'),
    path('Readmore/<str:slug>', views.News_readmore, name='readmore'),
]
