from django.conf.urls import url

from . import views

app_name = 'dobby'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^home/(?P<userId>[0-9]+)/', views.home, name='home'),
	url(r'^profile/', views.profile, name='profile'),
	url(r'^login/', views.login, name='login'),
	url(r'^rating/', views.rating, name='rating'),
	url(r'^compTransaction/', views.compTransaction, name='compTransaction'),
	url(r'^pendTransaction/', views.pendTransaction, name='pendTransaction'),
	url(r'^pendingTeacher/', views.pendingTeacher, name='pendingTeacher'),
	url(r'^search/', views.search, name='search'),
	url(r'^showSearch/', views.showSearch, name='showSearch'),
]