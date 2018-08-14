from django.shortcuts import render , HttpResponse
from .models import *
from django.http import HttpResponseRedirect
from .form import MomentForm
# Create your views here.

def Index(request):
    indexlist = IndexModels.objects.all()
    footqrcode = Footinfo.objects.all()
    bannerlist = IndexBanner.objects.all()
    footimg = IndexFootImg.objects.all()
    # print(indexlist)
    return render(request,'dota/index.html',{'indexlist':indexlist,'footqrcode':footqrcode,'bannerlist':bannerlist,'footimg':footimg})

def Aaboutus(request):
    aboutimg = AboutDetail.objects.all()
    # print(indexlist)
    return render(request,'dota/about.html',{'aboutimg':aboutimg})

def Newinfodetail(request):
    newlist = Newinfo.objects.all()
    # print(indexlist)
    return render(request,'dota/new.html',{'newlist':newlist})

def Teaminfodetail(request):
    teamlist = TeamInfo.objects.all()
    # print(indexlist)
    return render(request,'dota/team.html',{'teamlist':teamlist})

def Curlture(request):
    culturelist = CultuerDetaul.objects.all()
    # print(indexlist)
    return render(request,'dota/culture.html',{'culturelist':culturelist})

def Contact(request):
    contactlist = ContactDetail.objects.all()
    citylist = T_Area.objects.all()
    areaNamelist = T_Area.objects.filter(level = 1)
    level2 = T_Area.objects.filter(level=2  )
    level3 = T_Area.objects.filter(level=3)
    # print(indexlist)
    return render(request,'dota/contact.html',{'contactlist':contactlist,'citylist':citylist,'areaNamelist':areaNamelist,'level2':level2,'level3':level3})

def Form(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            if moment.content == 'a':
                print('content not nlll')
                return  HttpResponseRedirect('/index/')

    else:
        form = MomentForm
        return  render(request,'dota/form.html',{'form':form})
