from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$',views.Index),
    url(r'^index/$',views.Index),
    url(r'^about/$',views.Aaboutus),
    url(r'^new/$', views.Newinfodetail),
    url(r'^team/$', views.Teaminfodetail),
    url(r'^culture/$', views.Curlture),
    url(r'^contact/$', views.Contact),
    url(r'^form/$',views.Form),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

