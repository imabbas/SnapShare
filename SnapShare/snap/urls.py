from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^(?P<user_id>[0-9]+)/$', views.user_profile, name='user'),
    url(r'^login/$', views.login, name="login"),
    # url(r'^logout/$', views.logout, name="logout"),
    url(r'^register/$', views.register, name="register"),


]
