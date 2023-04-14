
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('About/', views.About, name='about'),
    path('Services/', views.Services, name='services'),
    path('How_we_work/', views.How_we_work, name='how_we_work'),
    path('Why_us/', views.Why_us, name='why_us'),
]
