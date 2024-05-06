from django.urls import path
from .views import hey
urlpatterns = [
    path('',hey),
]