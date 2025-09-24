from django.shortcuts import render
from .models import User, Category, Product, ProductImage, Order, OrderItem, Payment, Address
from .serializers import UserSerializer, CategorySerializer, ProductSerializer, ProductImageSerializer, OrderSerializer, OrderItemSerializer, PaymentSerializer, AddressSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('email')
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            # Registration should be allowed for anyone
            permission_classes = [AllowAny]
        else:
            # All other operations require authentication
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = (JWTAuthentication,)
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = (JWTAuthentication,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # Fields you can filter by exact match
    filterset_fields = ['category', 'is_active', 'price', 'stock_quantity']
    # Fields to allow text search (partial matches)
    search_fields = ['name', 'description']
    # Fields you can order by
    ordering_fields = ['name', 'price', 'stock_quantity', 'created_at', 'updated_at']
    ordering = ['name']  # Default ordering for DRF
    
class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all().order_by('created_at')
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = (JWTAuthentication,)
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)
    
    # Users will view their own orders
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('created_at')
    
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all().order_by('created_at')
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)
    
    def get_queryset(self):
        return OrderItem.objects.filter(order__user=self.request.user).order_by('created_at')

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().order_by('-created_at')
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)
    
    def get_queryset(self):
        # Limit payments to those belonging to the current user's orders.
        return Payment.objects.filter(order__user=self.request.user).order_by('-created_at')
    
    def update(self, request, *args, **kwargs):
        """
        Block direct updates to a payment record.
        Payment status/amount should be set by the system or gateway.
        """
        return Response(
            {"detail": "Payments cannot be updated manually."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
        
    def partial_update(self, request, *args, **kwargs):
        """
        Also block PATCH requests.
        """
        return Response(
            {"detail": "Payments cannot be updated manually."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def destroy(self, request, *args, **kwargs):
        """
        Optional: prevent deletion of payment records.
        """
        return Response(
            {"detail": "Payments cannot be deleted."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
        
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('created_at')
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)
    
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user).order_by('created_at')
    
    def perform_create(self, serializer):
        # Ensure the address is tied to the logged-in user
        serializer.save(user=self.request.user)