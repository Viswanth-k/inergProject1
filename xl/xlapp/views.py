from django.http import HttpResponse
from django.shortcuts import render

from .models import Xlss, Sum


def xl(request):
    xl = Xlss.objects.all()
    for i in xl:
        a = Xlss.objects.get(API_WELL_NUMBER=i.API_WELL_NUMBER, QUARTER=1)
        b = Xlss.objects.get(API_WELL_NUMBER=i.API_WELL_NUMBER, QUARTER=2)
        c = Xlss.objects.get(API_WELL_NUMBER=i.API_WELL_NUMBER, QUARTER=3)
        d = Xlss.objects.get(API_WELL_NUMBER=i.API_WELL_NUMBER, QUARTER=4)
        oil = a.OIL + b.OIL + c.OIL + d.OIL
        gas = a.GAS + b.GAS + c.GAS + d.GAS
        brine = a.BRINE + b.BRINE + c.BRINE + d.BRINE
        sum = Sum.objects.create(API_WELL_NUMBER=i.API_WELL_NUMBER, OIL=oil, GAS=gas, BRINE=brine)
        sum.save()
    return HttpResponse("sumxl")


def index(request):

    return render(request, "index.html")


def show(request):
    if request.method == 'GET':
        well = request.GET['well']
    a = Sum.objects.get(API_WELL_NUMBER=well)
    return render(request, "show.html", {'a': a})
