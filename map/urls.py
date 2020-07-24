from django.contrib import admin
from django.urls import path
import mapapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mapapp.views.index, name="index"),
    path('map/kakao/', mapapp.views.kakao, name="kakao"),
    path('map/google/', mapapp.views.google, name="google"),
]
