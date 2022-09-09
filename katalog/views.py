from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalogue(request):
    isi_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': isi_katalog,
        'nama': 'Divany Harryndira',
        'npm': '2106701734'
    }
    return render(request, "katalog.html", context)