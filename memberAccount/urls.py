from django.urls import path
from . import views



urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login_user/', views.login_user, name='login_user'),
    path('login_message/', views.login_message, name='login_message'),
    path('logout_user/', views.logout_user, name='logout_user'),
    
]