from unicodedata import name
from django.urls import path

from core.views import home, update

urlpatterns = [
    path('',home,name='home'),
    path('update/<int:todo_id>/',update,name='update')
]
