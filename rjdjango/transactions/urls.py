from django.urls import path
from transactions import views

urlpatterns = [
    path('gov', views.List.as_view()),
    path('profile/', views.Profile.as_view()),
    path('order/', views.order),
]
