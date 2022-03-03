from django.contrib import admin
from django.urls import path
from biorhythm.views import HomePage

urlpatterns = [
    path('', HomePage, name='home'),
    path('admin/', admin.site.urls),
]
