from django.contrib import admin
from django.urls import path, include
import consume.urls as consume_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(consume_urls, namespace='consume'))
]
