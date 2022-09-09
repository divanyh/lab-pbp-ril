from django.urls import path
from katalog.views import show_catalogue

app_name = 'katalog'

urlpatterns = [ path('', show_catalogue, name='show_catalogue')]