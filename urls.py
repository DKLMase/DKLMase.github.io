from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home, name='home'),  # Add trailing slash
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),  # Add trailing slash
    path('task_management/', views.task_management, name='task_management'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    
    # Password reset views
    path('reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # Wellness views
    path('wellness-check/', views.wellness_check, name='wellness_check'),
    path('wellness-check-result/', views.wellness_check_result, name='wellness_check_result'),
    
    # View schedules
    path('view-schedules/', views.view_schedules, name='view_schedules'), 
    
    
    path('password-reset/', views.CustomPasswordResetRequestView.as_view(), name='password_reset'),

   
]
