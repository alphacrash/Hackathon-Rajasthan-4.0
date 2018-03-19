from django.urls import path
from transactions.views import List

urlpatterns = [
    path('', List.as_view()),
]
