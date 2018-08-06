from django.contrib import admin
from .models import *

# Register your models here.

class Indexinfo(admin.ModelAdmin):
    list_display = ('pk','logo','title')
    fieldsets = (
        ('info',{
            'fields':('logo','title')
        }),
    )


class BanerImgAdmin(admin.ModelAdmin):
    list_display = ('pk','bannerimg','imgad','adtext','adtextinfo')
    fieldsets = (
        ('img',{
            'fields':('bannerimg','imgad')
        }),
        ('text',{
            'fields':('adtext','adtextinfo')
        }),
    )

class FootinfoAdmin(admin.ModelAdmin):
    list_display = ('pk','lerfqrcode','rightqrcode')
    fieldsets = (
        ('qrcode',{
            'fields':('lerfqrcode','rightqrcode')
        }),
    )

class NewinfoAdmin(admin.ModelAdmin):
    list_display = ('pk','newtitle','newdetails','addtime','updatetime','isdelete')
    fieldsets = (
        ('newinfo',{
            'fields':('newtitle','newdetails')
        }),
        ('details', {
            'fields': ('updatetime', 'isdelete')
        }),
    )

class TeamInfoAdmin(admin.ModelAdmin):
    list_display = ('pk','teamimg','teamdetail')
    fields = ('teamimg','teamdetail')

class AboutAdmin(admin.ModelAdmin):
    list_display = ('pk','Ad_one','Ad_two','Ad_there')
    fields = ('Ad_one','Ad_two','Ad_there')

class CultureDetailAdmin(admin.ModelAdmin):
    list_display = ('pk','culture_one','culture_two','culture_there','top_title','top_detail','mid_title','mid_detail','button_title','button_detail')
    fieldsets = (
        ('img',{
           'fields':('culture_one','culture_two','culture_there')
        }),
        ('top',{
            'fields': ('top_title','top_detail')
        }),
        ('mid', {
            'fields': ('mid_title','mid_detail')
        }),

        ('button', {
            'fields': ('button_title','button_detail')
        }),
    )

class ContactDetailAdmin(admin.ModelAdmin):
    list_display = ('pk','AD_one','AD_two','top_title','top_detail','mid_title','mid_info','mid_detail')
    fieldsets = (
        ('img',{
           'fields':('AD_one','AD_two')
        }),
        ('detail',{
           'fields':('top_title','top_detail','mid_title','mid_info','mid_detail')
        }),
    )

class IndexBannerAdmin(admin.ModelAdmin):
    list_display = ('banner_a','banner_b','banner_c','banner_d','banner_e','banner_a_xiao','banner_b_xiao','banner_c_xiao','banner_d_xiao','banner_e_xiao','bannertext','bannerdetail','isdelete')
    fieldsets = (
        ('img',{
           'fields':('banner_a','banner_b','banner_c','banner_d','banner_e')
        }),
        ('imgdetail',{
            'fields': ('banner_a_xiao','banner_b_xiao','banner_c_xiao','banner_d_xiao','banner_e_xiao')
        }),
        ('text',{
           'fields':('bannertext','bannerdetail')
        }),
    )

admin.site.register(IndexModels,Indexinfo)
admin.site.register(BanerImg,BanerImgAdmin)
admin.site.register(Footinfo,FootinfoAdmin)
admin.site.register(Newinfo,NewinfoAdmin)
admin.site.register(TeamInfo,TeamInfoAdmin)
admin.site.register(AboutDetail,AboutAdmin)
admin.site.register(CultuerDetaul,CultureDetailAdmin)
admin.site.register(ContactDetail,ContactDetailAdmin)
admin.site.register(IndexBanner,IndexBannerAdmin)
