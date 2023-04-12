
from django.urls import path
from .views import home, about, classes, team, galery, contact, article,  article_detail, booking
# from django.contrib.auth.views import LoginView
from django.contrib import admin

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls, name="admin"),

    path('about/', about, name="about"),
    path('class/', classes, name="class"),
    path('galery/', galery, name="galery"),
    path('team/', team, name="team"),
    path('contact/', contact, name="contact"),
    path('booking/<int:pk>/', booking, name="booking"),
    path('article/', article, name="article"),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    
]
