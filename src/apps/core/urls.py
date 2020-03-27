from django.urls import path

from apps.core.views import home, historico

urlpatterns = [
    path('', home, name='home'),
    path('historico/', historico, name='historico'),
]
