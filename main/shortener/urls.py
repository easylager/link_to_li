from django.contrib import admin
from django.urls import path, re_path
import re

from .views import *

urlpatterns = [
    path('', home, name='home_url'),
    path('login/', user_login, name='login_url'),
    path('register/', register, name='register_url'),
    path('transform_domain/', transform_domain, name='transform_domain_url'),
    path('my_links/', my_links, name='my_links_url'),
    re_path(r'^(?P<slug>\w{6})/$', redirect_to_origin, name='redirect_url')

]