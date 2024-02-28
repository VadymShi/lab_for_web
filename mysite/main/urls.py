from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addworker', views.add_work, name='addwork'),
    path('delworker', views.del_worker, name='delete_worker'),
    path('salary', views.sal, name='salary'),
    path('addoffice/', views.add_office, name='addoffice'),
    path('deloffice', views.deloffice, name='del_office'),
]