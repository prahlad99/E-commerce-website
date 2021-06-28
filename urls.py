from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path("",views.home,name='shophome'),

    path("abouts/",views.abouts,name='abouts'),
    path("contact/",views.contact,name='abouts'),
    path("tracker/",views.tracker,name='tracker'),
    path("checkout/",views.checkout,name='checkout'),
    path("products/<int:id>",views.prodview,name='productview'),
    path("search/",views.search,name='search'),
    path("handlerequest/",views.handlerequest,name='handlerequest'),

]
