from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('what-we-do/', views.what_we_do, name='what_we_do'),
    path('about/', views.about, name='about'),
    path('partners/', views.partners, name='partners'),
    path('contacts/', views.contacts, name='contacts'),
    path('blogs/', views.blogs, name='blogs'),
    ]