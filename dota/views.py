from django.shortcuts import render , HttpResponse
from .models import *
from .forms import Moment
from django.http import HttpResponseRedirect
# Create your views here.

def Index(request):
    indexlist = IndexModels.objects.all()
    footqrcode = Footinfo.objects.all()
    bannerlist = IndexBanner.objects.all()
    # print(indexlist)
    return render(request,'dota/index.html',{'indexlist':indexlist,'footqrcode':footqrcode,'bannerlist':bannerlist})

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
    # print(indexlist)
    return render(request,'dota/contact.html',{'contactlist':contactlist})

def MomentViews(request):
    if request.method == 'POST':
        form = Moment(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect('/index/')
    else:
        form = Moment()
        return render(request,'dota/form.html',{'form':form})
