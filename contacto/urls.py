from django.urls import path
from contacto import views


urlpatterns = [
    path('contact/', views.contact, name ='contact'),
]
