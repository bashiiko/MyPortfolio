from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.edit, name='edit'),
    path('show/', views.show_all_post, name='show'),
    path('update/', views.update, name='update'),
]
