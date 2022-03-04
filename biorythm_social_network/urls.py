from django.contrib import admin
from django.urls import path
from biorhythm.views import HomePage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePage, name='home'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
