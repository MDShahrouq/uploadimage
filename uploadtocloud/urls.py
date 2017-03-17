from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from uploadtocloud import views

urlpatterns = [
    url(r'^uploadtocloud/$', views.UploadtoimageList.as_view()),
    url(r'^uploadtocloud/(?P<pk>[0-9]+)/$', views.UploadtoimageDetail.as_view()),
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)
