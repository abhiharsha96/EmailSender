from django.contrib import admin
from django.urls import path,include
from emailSend import views
urlpatterns = [
    path('',views.greetings),
    path('contact',views.contact)
]