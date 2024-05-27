from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path('evenements/<str:url>/', views.event_detail, name='event_detail'),
    path('evenements/', views.events, name='events'),
    path('histoire/', views.history, name='history'),
    path('galerie', views.galerie, name='galerie'),
    path('galerie/<str:url>/', views.galerie_collection, name='galerie_collection'),
    path('contact', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
