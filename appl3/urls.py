from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gull/', asosiy1),
    path('mevaa/', asosiy2),
    path('cube/', cube),
]
