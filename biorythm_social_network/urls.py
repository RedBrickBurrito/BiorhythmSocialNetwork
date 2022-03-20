from django.contrib import admin
from django.urls import path
from biorhythm.views import HomePage
from user.views import SignUpPage
from django.conf import settings
from django.conf.urls.static import static
from user.views import CustomLoginView
from django.contrib.auth.views import LogoutView
from biorhythm.views import HomePage, Top3
from user.models import add_friend

urlpatterns = [
    path('signup/', SignUpPage, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', HomePage, name='home'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('top3/', Top3, name="top3"),
    path('admin/', admin.site.urls),
    path('add_friend/<int:user_id>/', add_friend, name='add_friend'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
