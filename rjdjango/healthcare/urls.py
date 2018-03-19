from django.urls import path
from healthcare import views

urlpatterns = [
    path('profile/', views.Profile.as_view()),
    
]
