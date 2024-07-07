
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.stockPicker, name = 'stockpicker'),
    path('about', views.aboutus, name='about'),
    path('contact', views.contactus, name='contact'),
    path('company', views.company, name='company'),
    path('stocktracker/', views.stockTracker, name = 'stocktracker'),
]