from django.urls import path # type: ignore
from . import views # type: ignore

urlpatterns = [
	path('', views.index, name='index'),
	path('counter', views.counter, name='counter'),
	path('register', views.register, name='register'),
]