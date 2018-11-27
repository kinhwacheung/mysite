from django.conf.urls import url

urlpatterns=patterns('',
        url(r'^archive/$','mysite.views.archive'),
        url(r'^about/$','mysite.views.about'),
        url(r'rss/$','mysite.views.rss'),
)
