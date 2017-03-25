from django.conf.urls import url

from . import views

app_name = 'dobby'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	# url(r'^updateGoogleId/', views.updateGoogleId, name='updateGoogleId'),
	# url(r'^googleIdExistsInDB/', views.googleIdExistsInDB, name='googleIdExistsInDB'),
]