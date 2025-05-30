from django.urls import path
from drf_spectacular.utils import extend_schema
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users import views

app_name = 'users'

TokenObtainPairView = extend_schema(tags=['Токены'])(TokenObtainPairView)
TokenRefreshView = extend_schema(tags=['Токены'])(TokenRefreshView)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = DefaultRouter()

router.register('', views.UserView, 'users')

urlpatterns += router.urls
