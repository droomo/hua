"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hua.driver import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^driver/check-driver-number/', views.check_number),
    url(r'^driver/update-info/', views.update_info),

    url(r'^follow/get-location', views.get_location, name='get_all_driver_location'),
    url(r'^follow/', views.follow),
]
