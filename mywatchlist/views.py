from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    isi_watchlist = WatchlistItem.objects.all()
    context = {
        'list_film': isi_watchlist,
        'nama': 'Divany Harryndira',
        'npm': '2106701734'
    }
    return render(request, "mywatchlist.html", context)

def export_to_json(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type = "application/json")
