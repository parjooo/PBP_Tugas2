from django.shortcuts import render
from mywatchList.models import WatchList
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    data_watchlist = WatchList.objects.all()
    context = {
        'list_data': data_watchlist,
        'nama' : 'Faris Bayhaqi'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
