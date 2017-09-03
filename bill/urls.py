from django.conf.urls import url
from . import views

app_name = 'bill'

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^quant$', views.quant, name = 'quant'),
]