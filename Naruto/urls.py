from django.urls import path
from Naruto.views import *

app_name = ''

urlpatterns=[
    path('Naruto/',Naruto,name='Naruto')
]