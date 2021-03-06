"""kernel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.v1.urls')),
    re_path(r'^', include('pages.urls')),
    re_path(r'^news/', include('news.urls')),
    re_path(r'^analyze/', include('analysis.urls')),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^accounts/', include("django.contrib.auth.urls")),
    re_path(r'^dashboard/', include("dashboard.urls")),
    re_path(r'^tutorials/', include('shop.urls')),
    re_path(r'^cart/', include('cart.urls')),
    re_path(r'^primarymarket/', include('primarymarket.urls')),
    re_path(r'^feeds/', include('feeds.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
