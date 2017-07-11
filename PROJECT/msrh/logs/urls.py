from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^test/', views.test, name='test'),
    url(r'^make/$', views.maketraining,name='make'),
    url(r'^show/', views.shows,name='show'),
    url(r'^addt/$', views.make, name='addtrain'),
    url(r'^request/$', views.request_training,name='request'),
    url(r'^req/',views.req_training,name="req_training"),
    url(r'^showpending/', views.pending, name="showpending"),
    url(r'^apply/', views.apply, name="apply")
    #url(r'^pop/',views.asdf)
]