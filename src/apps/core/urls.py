from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('historico/', views.historico, name='historico'),
]
