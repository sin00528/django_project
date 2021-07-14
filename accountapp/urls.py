from django.contrib import admin
from django.urls import path, include

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    # name = '___'는 라우트의 이름을 지정
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create')
]
