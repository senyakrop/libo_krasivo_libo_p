from . import views
from django.urls import path, include


urlpatterns = [
    path('allrating/', views.rating, name = "allrating"),
    path('', views.home, name='home'),
    path('signup/', views.SignUpGeneral.as_view(), name='signup'),
    path('signup_hr/', views.SignUpHR.as_view(), name='signup_hr'),
    path('signup_pm/', views.SignUpPM.as_view(), name='signup_pm'),
    path('signup_participant/', views.SignUpParticipant.as_view(), name='signup_participant'),
]
