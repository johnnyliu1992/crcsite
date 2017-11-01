from django.conf.urls import url

from . import views

urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^ra/$', views.ra, name='ra'),
               url(r'^raresult/$', views.raresult, name='raresult'),
               url(r'^explain/$', views.explain, name='explain'),
               url(r'^appo/$', views.appo, name='appo'),
               url(r'^screen/$', views.screen, name='screen'),
               url(r'^treatment/$', views.treatment, name='treatment'),
               url(r'^others/$', views.others, name='others'),
               url(r'^api/jfj', views.jfj, name='jfj'),
               ]