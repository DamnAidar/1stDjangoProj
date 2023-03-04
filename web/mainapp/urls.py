from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),    #круглые скобки не нужны что бы сразу не выполнять метод
    path('about', views.about),
    path('contacts', views.contacts),
    path('wtf', views.wtf),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
