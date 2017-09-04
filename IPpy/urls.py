"""IPpy URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from IPpy.view import scan
from IPpy.view import view
from IPpy.view import index
from IPpy.view import occupy
from IPpy.view import available
from IPpy.view import register

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index.index),

    url(r'^index$', index.index),
    url(r'^occupy', occupy.index),
    url(r'^available', available.index),
    url(r'^register', register.index),
    url(r'^scan', scan.index),

    url(r'^hello$', view.hello),
    url(r'^hello$', view.hello),
    url(r'^hello2$', view.hello2),
    url(r'^testdb$', view.testdb),
]
