from django.urls import path
from . import views
urlpatterns = [
    path('',view.home,name='name')
]
