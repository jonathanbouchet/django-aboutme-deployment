from django.conf.urls import url
from main_menu import views

#template tagging
app_name = 'main_menu'

urlpatterns = [
	url(r'^relative/$',views.relative,name='relative'),
	url(r'^CV/$',views.CV,name='CV'),
	url(r'^projects/$',views.projects,name='projects')
]