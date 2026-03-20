from django.urls import path
from .views import RegistroViews,LoginViews,LogoutViews,pagina_registro,pagina_login,pagina_logout,pagina_inicio

urlpatterns = [
    path('api/registro/', RegistroViews.as_view(), name='api-registro'),
    path('api/login/', LoginViews.as_view(), name='api_login'),
    path('api/logout/', LogoutViews.as_view(), name='api_logout'),

    path('registro/', pagina_registro, name='registro'),
    path('login/', pagina_login, name='login'),
    path('logout/', pagina_logout, name='logout'),
    path('home/',pagina_inicio,name='home'),
]
