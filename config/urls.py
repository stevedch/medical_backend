"""medical_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView
from rest_framework import routers

from appcore.api.viewset.auth import AuthViewSet
from appcore.api.viewset.ticket import TicketViewSet

router = routers.DefaultRouter()
router.register(r'ticket', TicketViewSet)
router.register(r'auth', AuthViewSet)

urlpatterns = [
    # ADMIN
    url('^admin/', admin.site.urls),

    # AUTH
    url(r'^$', LoginView.as_view(template_name='auth/login.html'), name='login'),

    # API RESTFRAMEWORK
    url('^api/', include(router.urls)),
]
