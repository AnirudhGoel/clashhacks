from django.conf.urls import url

from . import views

app_name = 'dobby'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^home/(?P<userId>[0-9]+)/', views.home, name='home'),
	url(r'^profile/', views.profile, name='profile'),
	url(r'^login/', views.login, name='login'),
	url(r'^rating/', views.rating, name='rating'),
	url(r'^compTrans/', views.compTrans, name='compTrans'),
	url(r'^pendingTeacher/', views.pendingTeacher, name='pendingTeacher'),
	url(r'^ongTrans/', views.ongTrans, name='ongTrans'),
	url(r'^search/(?P<userId>[0-9]+)/', views.search, name='search'),
	url(r'^showSearch/', views.showSearch, name='showSearch'),
	url(r'^pendingToOngoing/', views.pendingToOngoing, name='pendingToOngoing'),
	url(r'^pendingToReject/', views.pendingToReject, name='pendingToReject'),
	url(r'^ongoingToComplete/', views.ongoingToComplete, name='ongoingToComplete'),
	url(r'^addToPending/', views.addToPending, name='addToPending'),
]