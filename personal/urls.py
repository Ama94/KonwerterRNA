from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^converter/', include('converter.urls'), name='converter'),
    url(r'^contact/', views.contact, name='contact'),
]
