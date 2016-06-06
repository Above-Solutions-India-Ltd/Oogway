from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^servermonitor', views.Servermonitor, name="servermonitor"),
    url(r'^monitorlist', views.Monitorlist, name="monitorlist"),
    url(r'^monitordetailscheck_mem/', views.MonitorCheckMemory, name="monitordetailscheck_mem"),
    url(r'^monitordetailscheck_cpu/', views.MonitorCheckCpu, name="monitordetailscheck_cpu"),

]