"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib.auth import views as authentification_views
from courses.views import home

urlpatterns = [
    url(r'^$',home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')), # new
    url(r'^admin/', admin.site.urls),
    url(r'^course/', include('courses.urls')),
    url(r'^students/', include('students.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

