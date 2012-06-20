from django.conf.urls.defaults import *

urlpatterns = patterns('profile.views',
    url(r'^list_user/$', 'list_userids', name="list_userids"),
    url(r'^$', 'edit_profile', name="edit_profile"),
    url(r'^logout/$', 'logout_relay', name="logout_relay"),
)
