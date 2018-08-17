from django.shortcuts import render , HttpResponse
from .models import *
from django.http import HttpResponseRedirect
from .form import MomentForm
from django.core.paginator import Paginator ,EmptyPage ,PageNotAnInteger
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
    newlist = Newinfo.objects.order_by('-id')
    #按ID 号进行排序
    paginator = Paginator(newlist,5)
    #每页返回多少条数据
    page = request.GET.get('page')
    #从前端获取当前页码数
    try:
        newlist = paginator.page(page)
        #获取当前页码数的数据
    except PageNotAnInteger:
        newlist = paginator.page(1)
        #如果用户输入的不是整数返回第一页的数据
    except EmptyPage:
        newlist = paginator.page(paginator.num_pages)
        #如果用户输入超出最后一页 显示最后一页内容

    # print(indexlist)
    return render(request,'dota/new.html',{'newlist':newlist})



def Newport(request,id):
    new = Newinfo.objects.get(id = str(id))
    #根据获取的ID 显示相应内容
    return render(request,'dota/newport.html',{'new':new})



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
