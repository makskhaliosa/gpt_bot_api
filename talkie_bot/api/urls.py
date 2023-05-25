from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView)

from .views import (
    TgUserViewSet, UserMessageViewSet, GPTMessageViewSet,
    TariffViewSet, PaymentViewSet
)

router = DefaultRouter()

router.register(r'tg_users', TgUserViewSet)
router.register(r'tariffs', TariffViewSet)
router.register(r'gpt_messages', GPTMessageViewSet)
router.register(
    r'tg_users/(?P<username>[\w.@+-]+)/payments',
    PaymentViewSet,
    basename='payments'
)
router.register(
    r'tg_users/(?P<username>[\w.@+-]+)/user_messages',
    UserMessageViewSet,
    basename='user_messages'
)


urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
]
