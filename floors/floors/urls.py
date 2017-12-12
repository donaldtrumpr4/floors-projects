from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import floors.floors_blogs.urls as rrr

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include(rrr))
]
