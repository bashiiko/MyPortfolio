from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('create_user/', views.create_user, name='create_user'),
    path('add_works/', views.add_works, name='add_works'),
    path('show_works/', views.show_all_post_works, name='show_works'),
    path('update_works/', views.update_works, name='update_works'),
    path('add_activity/', views.add_activity, name='add_activity'),
    path('show_activity/', views.show_all_post_activity, name='show_activity'),
    path('update_activity/', views.update_activity, name='update_activity'),
]
