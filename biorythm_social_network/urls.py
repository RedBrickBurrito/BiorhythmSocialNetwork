from django.contrib import admin
from django.urls import path
from biorhythm.views import HomePage, Top3
from user.models import add_friend

urlpatterns = [
    path('', HomePage, name='home'),
    path('top3', Top3, name="top3"),
    path('admin/', admin.site.urls),
    path('add_friend/<int:user_id>/', add_friend, name='add_friend'),
]
