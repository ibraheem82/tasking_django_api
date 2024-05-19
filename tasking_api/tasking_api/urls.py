"""tasking_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from users import router as users_api_router


auth_api_urls  = [
    path(r'', include('rest_framework_social_oauth2.urls')),
]
if settings.DEBUG:
    #  This block is checking if the application is running in debug mode. If it is, it adds a URL pattern to the auth_api_urls list. This pattern includes all the URLs defined in rest_framework.urls, which provides views for login, logout, and password change. The r'verify/' part means that these views will be accessible at URLs that start with verify/.
    auth_api_urls.append(path(r'verify/', include('rest_framework.urls')))


api_url_patterns = [
    #  This line is adding a URL pattern that includes all the URLs in auth_api_urls. The auth/ part means that these URLs will be accessible at URLs that start with auth/.
    path('auth/', include(auth_api_urls)),
    path('accounts/', include(users_api_router.router.urls))
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns))
]
