from django.urls import path
from emitra import views

app_name = 'emitra'
urlpatterns = [
    path('profile/', views.Profile.as_view(), name='profile'),
]