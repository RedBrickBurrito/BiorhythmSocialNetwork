from django.contrib import admin
from django.urls import path
from biorhythm.views import HomePage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomePage, name='home'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('admin/', admin.site.urls),
]
