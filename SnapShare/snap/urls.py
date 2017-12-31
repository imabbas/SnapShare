from django.conf.urls import url
from . import views

app_name = "snap"

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    # url(r'^(?P<user_id>[0-9]+)/$', views.user_profile, name='user'),
    url(r'^login/$', views.LoginFormView.as_view(), name="login"),
    # url(r'^logout/$', views.logout, name="logout"),
    url(r'^register/$', views.RegisterFormView.as_view(), name="register"),
    url(r'^add/$', views.PostCreate.as_view(), name="post-add"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')



]
