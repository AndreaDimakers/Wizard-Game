from django.urls import path
from .views import RegistroViews, pagina_registro

urlpatterns = [
    path('api/registro/', RegistroViews.as_view(), name='api-registro'),
    path('registro/', pagina_registro, name='registro'),
]

