from django.urls import path
from .views import GetTenPizzasView, index, random

app_name = 'pizza'
urlpatterns = [
    path('<int:pid>/', index, name='detail'),
    path('random/', random, name='random'),
    path('ten', GetTenPizzasView.as_view(), name='ten'),
]
