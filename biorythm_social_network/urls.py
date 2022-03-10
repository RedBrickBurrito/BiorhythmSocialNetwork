from django.contrib import admin
from django.urls import path
from biorhythm.views import HomePage
from user.views import SignUpPage
from django.conf import settings
from django.conf.urls.static import static
from user.views import CustomLoginView

urlpatterns = [
    path('signup/', SignUpPage.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', HomePage, name='home'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
