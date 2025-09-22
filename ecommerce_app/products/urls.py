from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, CategoryViewSet, ProductViewSet,
    ProductImageViewSet, OrderViewSet, OrderItemViewSet,
    PaymentViewSet, AddressViewSet
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('product-images', ProductImageViewSet)
router.register('orders', OrderViewSet)
router.register('order-items', OrderItemViewSet)
router.register('payments', PaymentViewSet)
router.register('addresses', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]