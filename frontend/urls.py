from django.urls import path
from frontend import views

urlpatterns = [
    path('home/', views.index, name ='home'),
    path('porfolio/', views.portfolio, name ='portfolio'),
    path('about/', views.about, name ='about'),
    path('work/', views.work, name ='work'),

]
