from django.urls import path 
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('checkin/', views.checkin, name='checkin'),
	path('<int:pk>/lobby/', views.lobby, name='lobby'),
	path('host/', views.host, name='host'),
	path('host/manage/', views.host_manage, name='host_manage'),
	path('host/login/', views.hostlogin, name='hostlogin'),
]
