"""tribune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import re_path as url
from django.urls import include,reverse_lazy
from django.contrib import admin
from django.contrib.auth import views
from django.views.generic.edit import CreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('new.urls')),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/register/',CreateView.as_view(template_name='django_registration/registration_form.html',success_url =reverse_lazy('login') )),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/login/',views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    url(r'^logout/$',views.LogoutView.as_view(next_page ='newsToday')),
    url(r'^tinymce/', include('tinymce.urls')),
]

