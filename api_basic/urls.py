from django.urls import path
from .views import state, home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home),
    path('state/', state)
]

urlpatterns += staticfiles_urlpatterns()