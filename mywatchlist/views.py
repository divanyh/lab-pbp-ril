from django.shortcuts import render
from mywatchlist.models import WatchlistItem

# Create your views here.
def show_watchlist(request):
    isi_watchlist = WatchlistItem.objects.all()
    context = {
        'list_film': isi_watchlist,
        'nama': 'Divany Harryndira',
        'npm': '2106701734'
    }
    return render(request, "mywatchlist.html", context)