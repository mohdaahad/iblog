from django.contrib import admin
from django.urls import path,include
from app import  views
urlpatterns = [
    
     path('',views.home ,name='home'),
     path('app/<int:id>',views.post, name='post_detail'),
     path('signin', views.user_login, name='login'),
     path('signup/', views.signup, name='signup'),
     path('report-about/', views.report, name='report'),
     path('contacts/', views.contacts, name='contacts'),
     path('logout/', views.user_logout, name='logout'),
     path('category/<slug:url>',views.category),
     path('about/',views.about ,name='about'),
     path('likepost/',views.likepost ,name='likepost'),
     path('tags/',views.tags ,name='tags'),
     path('createpost/',views.createpost ,name='createpost'),
     path('singout_confirm/',views.signout ,name='singout'),
     path('profile/<slug:username>/',views.userprofile ,name='userprofile'),
     path('post/<slug:user_id>',views.postuserprofile ,name='postuserprofile'),
     path('setting_profile/',views.editprofile ,name='setting_profile'),
 
]
