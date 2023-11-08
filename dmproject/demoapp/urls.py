
from django.urls import path,include

from demoapp import views

urlpatterns = [

    path('',views.home,name='home'),

    # path('operations/', views.operation, name='operation'),
    # #path('contact/', views.contact, name='contact'),
    # #path('detail/', views.detail, name='detail'),
    # #path('thanks/', views.thanks, name='thanks'),

]
