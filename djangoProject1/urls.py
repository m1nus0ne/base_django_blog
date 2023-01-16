from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('mainblog.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('members.urls'))

]