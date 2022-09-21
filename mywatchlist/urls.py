from django.urls import path
from mywatchlist.views import show_watchlist
from mywatchlist.views import export_to_json
from mywatchlist.views import export_to_xml

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    path('html/', show_watchlist, name='show_watchlist'),
    path('json/', export_to_json, name = 'export_to_json'),
    path('xml/', export_to_xml, name = 'export_to_xml'),
]
