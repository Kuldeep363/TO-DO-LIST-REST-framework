
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('listFrontEnd.urls')),
    path('api/',include('api.urls')),
    path('accounts/',include('accounts.urls')),
]
