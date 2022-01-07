from django.urls import path
from cat import views

from cat.views import home









urlpatterns = [
    path('',views.home),
]
