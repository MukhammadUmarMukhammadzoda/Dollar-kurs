from django.shortcuts import render,redirect
from .models import Kurs
from django.contrib.auth.decorators import login_required
from . import scrap


def index(request):
    data = Kurs.objects.all()
    
    return render(request, 'index.html', {'datas':data})


@login_required
def refresh(request):
    Kurs.objects.all().delete()
    data = Kurs(bank="HamkorBank", dollar_olish=scrap.hamkorbank_dollar_olish,
                dollar_sotish=scrap.hamkorbank_dollar_sotish,
                euro_olish=scrap.hamkorbank_euro_olish,
                euro_sotish=scrap.hamkorbank_euro_sotish)
    data.save()
    data2 = Kurs(bank="Milliy Bank", dollar_olish=scrap.mdo,
                dollar_sotish=scrap.mdb,
                euro_olish=scrap.meo,
                euro_sotish=scrap.meb)
    data2.save()
    data3 = Kurs(bank="Sanoat Qurilish Bank", dollar_olish=scrap.sqb_do,
                dollar_sotish=scrap.sqb_db,
                euro_olish=scrap.sqb_eo,
                euro_sotish=scrap.sqb_eb)
    data3.save()
    return redirect('index')

def xatolik(request):
    return render(request,'hatolik.html')