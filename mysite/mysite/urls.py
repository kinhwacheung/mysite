"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path
from django.conf.urls import url
# from django.conf import settings
from mysite.views import hello,current_datetime,hours_ahead,current_url_view_good,display_meta
from mysite.books.views import search,contact,thanks


urlpatterns = [
    url('admin/',admin.site.urls),
    url(r'^hello/$',hello),
    url(r'^time/$',current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^curpath/$',current_url_view_good),
    url(r'^allmeta/$',display_meta),
   # url(r'^search-form/$',search_form),
    url(r'^search/$',search),
    url(r'^contact/$',contact),
    url(r'thanks/$',thanks),
    url(r'^events/$',mysite.books.views.object_list,{'model':mysite.books.models.Event}),
    url(r'^blog/entries/$',mysite.books.views.object_list,{'model':mysite.books.models.BlogEntry}),
    url(r'^somepage/$',views.method_splitter,{'GET':mysites.books.views.some_page_get,'POST':mysite.books.views.some_page_post)
]

'''
if settings.DEBUG:
    urlpatterns+=patterns('',
    url(r'^debuginfo/$',mysite.views.debug),
    )
'''
