from django.urls import path
from land import views

urlpatterns = [
    path('profile/', views.Profile.as_view()),
]