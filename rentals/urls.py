from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_list),
    path('cars/<int:id>', views.car_details),
    path('signup/', views.signup_user, name='signup_user'),
    path('login/', views.login_user, name='login_user'),
]