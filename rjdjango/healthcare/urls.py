from django.urls import path
from healthcare import views

app_name = 'health'
urlpatterns = [
    path('profile/', views.Profile.as_view(), name='profile'),
    
]
