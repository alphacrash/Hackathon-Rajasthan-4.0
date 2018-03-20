from django.urls import path
from transactions import views

urlpatterns = [
    path('', views.List.as_view()),
    path('all/', views.Profile.as_view()),
]
