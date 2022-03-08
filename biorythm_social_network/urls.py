from django.contrib import admin
from django.urls import path
from biorhythm.views import HomePage


from user.views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', HomePage, name='home'),
    path('admin/', admin.site.urls),
]
