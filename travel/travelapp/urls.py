from . import views
from django.urls import path

urlpatterns = [
    path('',views.inde,name='index'),


   ]