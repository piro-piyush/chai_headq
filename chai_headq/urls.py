"""
URL configuration for chai_headq project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

# Url : localhost:8080/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('tweet.urls'),name='home'),
    path('tweet/',include('tweet.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
