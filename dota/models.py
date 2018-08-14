from django.db import models
from tinymce.models import HTMLField
import tinymce

# Create your models here.

class IndexModels(models.Model):
    logo = models.ImageField(upload_to='media/',verbose_name='logo')
    title = models.CharField(max_length=120,verbose_name='网站标题')

    class Meta:
        verbose_name_plural = u'首页内容'

class BanerImg(models.Model):
    bannerimg = models.ImageField(upload_to='bannerimg/',verbose_name='广告图')
    imgad = models.ImageField(upload_to='bannerimg/',verbose_name='缩略图')
    adtext = models.CharField(max_length=120,verbose_name='banner标题')
    adtextinfo = models.CharField(max_length=120,verbose_name='banner详情')

    class Meta:
        verbose_name_plural = u'广告图片'


class Footinfo(models.Model):
    lerfqrcode = models.ImageField(upload_to='qrcode/',verbose_name='左侧二维码')
    rightqrcode = models.ImageField(upload_to='qrcode/',verbose_name='后侧二维码')

    class Meta:
        verbose_name_plural = u'底部二维码'


class Newinfo(models.Model):
    newtitle = models.CharField(max_length=120,verbose_name='新闻标题')
    newdetails = HTMLField(verbose_name='新闻详情')
    addtime = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')
    updatetime = models.DateTimeField(auto_now=False,verbose_name='修改时间')
    isdelete = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = u'新闻'

class TeamInfo(models.Model):
    teamimg = models.ImageField(upload_to='teamimg/',verbose_name='团队图片')
    teamdetail = models.CharField(max_length=120,verbose_name='详情介绍')

    class Meta:
        verbose_name_plural = u'团队'



class AboutDetail(models.Model):
    Ad_one = models.ImageField(upload_to='ad/',verbose_name='广告图1')
    Ad_two = models.ImageField(upload_to='ad/',verbose_name='广告图2')
    Ad_there = models.ImageField(upload_to='ad/', verbose_name='广告图3')

    class Meta:
        verbose_name_plural = u'关于我们广告图'

class CultuerDetaul(models.Model):
    culture_one = models.ImageField(upload_to='culture/',verbose_name='广告图1')
    top_title = models.CharField(max_length=120,verbose_name='顶部标题')
    top_detail = HTMLField(verbose_name='顶部详情')
    culture_two = models.ImageField(upload_to='culture/',verbose_name='广告图2')
    mid_title = models.CharField(max_length=120,verbose_name='中部标题')
    mid_detail = HTMLField(verbose_name='中部详情')
    culture_there = models.ImageField(upload_to='culture/', verbose_name='广告图3')
    button_title = models.CharField(max_length=120,verbose_name='底部标题')
    button_detail = HTMLField(verbose_name='底部详情')

    class Meta:
        verbose_name_plural = u'文化'

class ContactDetail(models.Model):
    AD_one = models.ImageField(upload_to='contactad/',verbose_name='广告图1')
    top_title = models.CharField(max_length=120,verbose_name='顶部标题')
    top_detail = HTMLField(verbose_name='顶部详情')
    AD_two = models.ImageField(upload_to='contactad/', verbose_name='广告图2')
    mid_title = models.CharField(max_length=120,verbose_name='中部标题')
    mid_info = models.CharField(max_length=120,verbose_name='中部小标')
    mid_detail = HTMLField(verbose_name='中部详情')

    class Meta:
        verbose_name_plural = u'联系我们 '


class IndexBanner(models.Model):
    banner_a = models.ImageField(upload_to='banner/',verbose_name='首页广告1')
    banner_b = models.ImageField(upload_to='banner/', verbose_name='首页广告2')
    banner_c = models.ImageField(upload_to='banner/', verbose_name='首页广告3')
    banner_d = models.ImageField(upload_to='banner/', verbose_name='首页广告4')
    banner_e = models.ImageField(upload_to='banner/', verbose_name='首页广告5')
    banner_a_xiao = models.ImageField(upload_to='banner/xiao/',verbose_name='首页广告1小图')
    banner_b_xiao = models.ImageField(upload_to='banner/xiao/', verbose_name='首页广告2小图')
    banner_c_xiao = models.ImageField(upload_to='banner/xiao/', verbose_name='首页广告3小图')
    banner_d_xiao = models.ImageField(upload_to='banner/xiao/', verbose_name='首页广告4小图')
    banner_e_xiao= models.ImageField(upload_to='banner/xiao/', verbose_name='首页广告5小图')
    bannertext = models.CharField(max_length=120,verbose_name='banner文字')
    bannerdetail = models.CharField(max_length=120,verbose_name='小字')
    isdelete = models.BooleanField(default=False,verbose_name='是否可删除')

    class Meta:
        verbose_name_plural = u'首页广告'


class IndexFootImg(models.Model):
    footimg_a = models.ImageField(upload_to='footimg/', verbose_name='底部图片1')
    footimg_b = models.ImageField(upload_to='footimg/', verbose_name='底部图片2')
    footimg_c = models.ImageField(upload_to='footimg/', verbose_name='底部图片3')
    footimg_d = models.ImageField(upload_to='footimg/', verbose_name='底部图片4')
    footimg_e = models.ImageField(upload_to='footimg/', verbose_name='底部图片5')
    footimg_a_xiao = models.ImageField(upload_to='footimg/xiao/',verbose_name='底部广告1小图')
    footimg_b_xiao = models.ImageField(upload_to='footimg/xiao/', verbose_name='底部广告2小图')
    footimg_c_xiao = models.ImageField(upload_to='footimg/xiao/', verbose_name='底部广告3小图')
    footimg_d_xiao = models.ImageField(upload_to='footimg/xiao/', verbose_name='底部广告4小图')
    footimg_e_xiao = models.ImageField(upload_to='footimg/xiao/', verbose_name='底部广告4小图')

    class Meta:
        verbose_name_plural = u'底部广告图'


KIND_CHOICES = (
    ('java','java'),
    ('php','php'),
    ('python','pyhon'),
    ('c++','c++'),
)

class UserKind(models.Model):
    content = models.CharField(max_length=120,verbose_name='提交内容')
    username = models.CharField(max_length=120,verbose_name='提交用户')
    kind_choices = models.CharField(max_length=120,choices=KIND_CHOICES,default=KIND_CHOICES[0])

    class Meta:
        verbose_name_plural = u'用户提交信息'

class T_Area(models.Model):
    areaId = models.IntegerField(verbose_name='地区Id')
    areaCode = models.CharField(max_length=20,verbose_name='地区编码')
    areaName = models.CharField(max_length=120,verbose_name='地区名')
    level =   models.IntegerField(verbose_name='地区级别')
    cityCode = models.CharField(max_length=20,verbose_name='城市编码')
    center = models.CharField(max_length=20,verbose_name='城市中心点')
    parentId = models.IntegerField(verbose_name='地区父节点')

    class Meta:
        verbose_name_plural = u'城市表'




