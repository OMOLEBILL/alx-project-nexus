"""
Module for creating serializers for Product application models
"""
from typing import Any
from rest_framework import serializers

from administration.models import Supplier
from products.models import Category, Product, Stock, SupplierProduct


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model
    """

    class Meta:
        model = Category
        fields = ["name", "uuid", "image", "thumbnail", "created_at", "updated_at"]


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model
    """

    #category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            "category",
            "name",
            "uuid",
            "code",
            "description",
            "product_type",
            "tax_type",
            "unit",
            "limited",
            "active_for_sale",
            "created_at",
            "updated_at",
            "packaging_unit",
        ]


class StockSerializer(serializers.ModelSerializer):
    """
    Serializer for Stock model
    """

    # Use the ProductSerializer as a nested serializer for the product_id field
    product_id = ProductSerializer(read_only=True)

    class Meta:
        model = Stock
        fields = [
            "product_id",
            "uuid",
            "stock_quantity",
            "created_at",
            "updated_at",
            "cost_per_unit",
            "price_per_unit_retail",
            "price_per_unit_wholesale",
            "reorder_level",
            "reorder_quantity",
            "stock_movement_type",
            "stock_movement_quantity",
            "stock_movement_remarks",
        ]

    def validate_stock_movement_type(self, value):
        """
        Ensure that stock_movement type is valid
        """
        valid_movement_types = [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
        ]
        if value not in valid_movement_types:
            raise serializers.ValidationError("Invalid stock movement type")
        return value

    def update(self, instance, validated_data):
        """
        update stock quantities accordingly
        """
        instance.update_stock_quantity(
            validated_data.get("stock_movement_type"),
            validated_data.get("stock_movement_quantity"),
            validated_data.get("stock_movement_remarks"),
        )

        return super().update(instance, validated_data)


class SupplierSerializer(serializers.ModelSerializer):
    """
    Serializer for Supplier model
    """

    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Supplier
        fields = [
            "uuid",
            "products",
            "name",
            "address",
            "email_address",
            "phone_number",
            "created_at",
            "updated_at",
        ]

    # def create(self, validated_data):
    #     """create and validate a supplier instance"""
    #     supplier = Supplier.objects.create(**validated_data)
    #     return supplier

    # def update(self, supplier, validated_data):
    #     """updates a supplier"""
    #     print(self.initial_data, "at update in seliaze")
    #     product_data = self.initial_data.pop("products")
    #     print("we got product data:", product_data)
    #     if product_data:
    #         #supplier.products.clear()
    #         for product in product_data:
    #             supplier.products.add(product)
    #     supplier.name = validated_data.get("name", supplier.name)
    #     supplier.address = validated_data.get("address", supplier.address)
    #     supplier.email_address = validated_data.get("email_address", supplier.email_address)
    #     supplier.phone_number = validated_data.get("phone_number", supplier.phone_number)
    #     print("supplier saved")
    #     supplier.save()
    #     return supplier


class SupplierProductSerializer(serializers.ModelSerializer):
    """
    Serializer for SupplierProduct model
    """

    class Meta:
        model = SupplierProduct
        fields = ["supplier", "product"]


class NotFoundSerializer(serializers.Serializer):
    detail = serializers.CharField(default="Unfortunately requested resource not found")
