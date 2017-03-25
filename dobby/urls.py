from django.conf.urls import url

from . import views

app_name = 'dobby'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^home/', views.home, name='home'),
	url(r'^profile/', views.profile, name='profile'),
	url(r'^login/', views.login, name='login'),
	url(r'^rating/', views.rating, name='rating'),
	url(r'^transaction/', views.transaction, name='transaction'),
	# url(r'^updateGoogleId/', views.updateGoogleId, name='updateGoogleId'),
	# url(r'^googleIdExistsInDB/', views.googleIdExistsInDB, name='googleIdExistsInDB'),
]