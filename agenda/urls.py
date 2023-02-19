from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('contatos/', include('contatos.urls'), name='contatos'),
    path('', include('contatos.urls'), name='contatos'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
