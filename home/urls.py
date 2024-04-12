from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('evenements/<str:url>/', views.event_detail, name='event_detail'),
    path('evenements/', views.events, name='events'),
    path('histoire/', views.history, name='history'),
    path('galerie', views.galerie, name='galerie'),
]
