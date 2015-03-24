from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import IndexView, EntradaDetailView
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^$', IndexView.as_view()),
    url(r'^entrada/(?P<slug>[-\w]+)/$', EntradaDetailView.as_view()),
)
