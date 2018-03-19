from django.urls import path
from land import views

app_name = 'land'
urlpatterns = [
    path('profile/', views.Profile.as_view(), name='profile'),
]