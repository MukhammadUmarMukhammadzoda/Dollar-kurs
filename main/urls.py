from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('refresh',views.refresh),
    path('xatolik',views.xatolik,name='xatolik')
    
]