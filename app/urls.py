from django.contrib import admin
from django.urls import path,include
from app import  views
urlpatterns = [
     path('tinymce/', include('tinymce.urls')),
     path('',views.home ,name='home'),
     path('app/<slug:url>',views.post, name='post_detail'),
     path('login/', views.user_login, name='login'),
     path('signup/', views.signup, name='signup'),
     path('report-about/', views.report, name='report'),
     path('contacts/', views.contacts, name='contacts'),
     path('logout/', views.user_logout, name='logout'),
     path('category/<slug:url>',views.category),
     path('about/',views.about ,name='about'),
     path('tags/',views.tags ,name='tags'),
     path('singout_confirm/',views.signout ,name='singout'),


 
]
