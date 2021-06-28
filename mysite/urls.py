from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('shop/',include('shop.urls')),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('',views.index),




    # path('rock',views.rock,name='rock'),
    # path('spaceremover',views.spaceremover,name='spaceremover'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)