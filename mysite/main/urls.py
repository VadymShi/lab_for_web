from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.dashboard, name='dashboard'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html',next_page=None),name='logout'),
    #path('password-change/',auth_views.PasswordChangeView.as_view(),name='password_change'),

 #path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(),
 #name='password_change_done'),
    #path('password-reset/',
         #auth_views.PasswordResetView.as_view(),
         #name='password_reset'),
    #path('password-reset/done/',
         #auth_views.PasswordResetDoneView.as_view(),
         #name='password_reset_done'),
    #path('password-reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),
 #name='password_reset_confirm'),
 #path('password-reset/complete/',
 #auth_views.PasswordResetCompleteView.as_view(),
 #name='password_reset_complete'),
    #path('', views.home, name='home'),
    #path('login', views.user_login, name='login'),
    path('addworker', views.add_work, name='addwork'),
    path('delworker', views.del_worker, name='delete_worker'),
    path('salary', views.sal, name='salary'),
    path('addoffice/', views.add_office, name='addoffice'),
    path('deloffice', views.deloffice, name='del_office'),
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]