from django.conf.urls import patterns, include, url
from django.contrib import admin

from HelloApp import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HelloProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),  # ADD NEW PATTERN!
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout')


)
