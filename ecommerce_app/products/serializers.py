from rest_framework import serializers
from .models import User, Category, Product, ProductImage, Order, OrderItem, Payment, Address

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    role = serializers.CharField(read_only=True)
    
    class Meta:
        model = User
        fields = ['user_id', 'email', 'first_name', 'last_name', 'phone_number', 'role', 
                  'password', 'created_at', 'updated_at']
        read_only_fields = ['user_id', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.full_clean()  # runs model.clean()
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        if password:
            instance.set_password(password)
        instance.full_clean()
        instance.save()
        return instance

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'name', 'description', 'parent', 'created_at']
        read_only_fields = ['category_id', 'parent', 'created_at']
        
    def validate_parent(self, value):
        if self.instance and value == self.instance:
            raise serializers.ValidationError("A category cannot be its own parent.")
        return value

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'description', 'price', 'stock_quantity', 'category',
                  'is_active', 'created_at', 'updated_at']
        read_only_fields = ['product_id', 'created_at', 'updated_at']
        
class ProductImageSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ProductImage
        fields = ['image_id', 'product', 'image_url', 'alt_text', 'created_at']
        read_only_fields = ['image_id', 'created_at']
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'user', 'status', 'total_amount', 'created_at', 'updated_at']
        read_only_fields = ['order_id', 'total_amount', 'created_at', 'updated_at']
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order_item_id', 'order', 'product', 'quantity', 'unit_price',
                  'subtotal', 'created_at']
        read_only_fields = ['order_item_id', 'subtotal', 'created_at']
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id', 'order', 'payment_method', 'payment_status', 'amount',
                  'transaction_id', 'created_at', 'updated_at']
        read_only_fields = ['payment_id', 'amount', 'transaction_id', 'payment_status', 
                            'created_at', 'updated_at']
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address_id', 'user', 'street', 'city', 'state', 'postal_code',
                  'country', 'is_default', 'created_at', 'updated_at']
        read_only_fields = ['address_id', 'user', 'created_at', 'updated_at']