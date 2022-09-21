from django.urls import path
from mywatchList.views import show_watchlist
from mywatchList.views import show_xml
from mywatchList.views import show_json

app_name = 'mywatchList'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    path('html/', show_watchlist, name='show_watchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]