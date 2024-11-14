from django.urls import path # type: ignore
from . import views # type: ignore

urlpatterns = [
	path('', views.index, name='index'),
	path('counter', views.counter, name='counter'),
	path('register', views.register, name='register'),
	path('login', views.log_in, name='login'),
	path('logout', views.log_out, name="logout"),
	path('play', views.play, name='play'),
]