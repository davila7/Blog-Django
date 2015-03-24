from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import IndexView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^$', IndexView.as_view()),
)
