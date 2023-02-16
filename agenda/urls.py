from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('contatos/', include('contatos.urls'), name='contatos'),
    path('', include('contatos.urls'), name='contatos'),
]
