from django.urls import path
from frontend import views

urlpatterns = [
    path('index/', views.index, name ='index'),
    path('porfolio/', views.portfolio, name ='portfolio'),
    path('about/', views.about, name ='about'),
    path('work/', views.work, name ='work'),

]