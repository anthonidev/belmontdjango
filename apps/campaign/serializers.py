from rest_framework import serializers

from .models import ListClient


class ListClientSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField(source="get_count")

    class Meta:
        model = ListClient
        fields = [
            'id',
            'title',
            'description',
            'updated_at',
            'status',
            'total'
        ]


# class CartItemSerializer(serializers.ModelSerializer):
#     product = ProductSerializer()

#     class Meta:
#         model = CartItem
#         fields = ['id', 'product', 'count', ]


# class CartSerializer(serializers.ModelSerializer):
#     items = CartItemSerializer(many=True)
#     amount = serializers.DecimalField(
#         source="get_amount", max_digits=10, decimal_places=2)
#     total_items = serializers.IntegerField(source="get_total_items")

#     class Meta:
#         model = Cart
#         fields = [
#             'id',
#             'total_items',
#             'items',
#             'amount'
#         ]
