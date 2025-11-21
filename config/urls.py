from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Настройка Swagger/OpenAPI
schema_view = get_schema_view(
   openapi.Info(
      title="Library API",
      default_version='v1',
      description="API для управления библиотекой",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Эндпоинты нашего приложения
    # Библиотека (книги, авторы, выдача, поиск)
    path('api/', include('library.urls')),
    # Пользователи (регистрация)
    path('api/users/', include('users.urls')),
    
    # JWT Авторизация
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Документация (Swagger и Redoc)
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
