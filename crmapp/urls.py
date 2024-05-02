from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('archive',views.archive,name='archive'),
    path('dashboardc',views.dashboardc,name='dashboardc'),
    path('archivec',views.archivec,name='archivec'),

]
