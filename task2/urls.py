from django.urls import path
from . import views

app_name = "people"

urlpatterns = [
    path('', views.secunpart, name='home'),
    path('<slug:slug>/', views.person_detail, name='person'),
]

