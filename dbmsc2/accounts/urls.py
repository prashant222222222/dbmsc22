from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name='accounts'

urlpatterns=[
    url(r'login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),
    name='login'),
    url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'signup/$',views.Signup.as_view(),name='signup'),
    url('^relative/$',views.relurl,name='relative'),
    url('^other/$',views.other,name='other'),
    url('^one/$',views.one,name='one'),
    url('^bihar/$',views.bihar,name='bihar'),
    url('^tamilnadu/$',views.tamilnadu,name='tamilnadu'),
    url('^up/$',views.up,name='up'),
    url('^karnataka/$',views.karnataka,name='karnataka'),
    url('^jammukashmir/$',views.jammukashmir,name='jammukashmir'),
        url('^home/$', views.home,name='home'),
url('^newpage/$',  views.new_page,  name="my_function"),
url('^users/$',  views.users,  name="users"),
url('^test/$',  views.test,  name="test"),
url('^thanks/$',  views.thanks,  name="thanks"),

]
