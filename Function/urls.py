from django.conf.urls import url

from . import views

app_name = 'functifunctionons'

urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'^add/$', views.AddFunction, name='add_function'),
    url(r'^search/$', views.TagSearch, name='tag_search'),
    url(r'^tag/(?P<tag>[\w-]+)/$', views.AllFunction_Tag, name='tag_functions'),
    url(r'^(?P<slug>[\w-]+)/$', views.ShowFunction, name='show_function'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.EditFunction, name='edit_function'),
    url(r'^(?P<slug>[\w-]+)/(?P<tag>[\w-]+)/remove/$', views.RemoveFunction_Tag, name='remove_function_tag'),
]