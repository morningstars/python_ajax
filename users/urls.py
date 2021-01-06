from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register', views.register),
    url(r'^checkuname', views.checkuname),
    url(r'^regUser', views.reguser),
    url(r'^query_users', views.query_users),
    url(r'^query_server', views.query_server),
    url(r'^jso$', views.jso),
    url(r'^json/$', views.json_views),
    url(r'^json_server/$', views.json_server),
    url(r'^front_json/$', views.front_json),
    url(r'^front_server/$', views.front_server),

    url(r'^01-load/$', views.load_views),
    url(r'^02-get/$', views.get_views),
    url(r'^02-server/$', views.server02),
    url(r'^03-post/$', views.post_views),
    url(r'^03-server/$', views.server03),
    url(r'^04-ajax/$', views.ajax_views),
    url(r'^04-server/$', views.server04),
]
