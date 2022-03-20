from django.contrib import admin
from django.urls import path
from biorhythm.views import HomePage
from user.views import SignUpPage
from django.conf import settings
from django.conf.urls.static import static
from user.views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', SignUpPage, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', HomePage, name='home'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
