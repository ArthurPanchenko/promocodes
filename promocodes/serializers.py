from rest_framework import serializers

from .models import Balance, Promocode


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = (
            'balance',
        )


class PromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = (
            'code',
            'amount'
        )


class CreatePromocodeSerializer(serializers.Serializer):
    count = serializers.IntegerField(min_value=1)
    prefix = serializers.CharField(max_length=9, required=False)
    amount = serializers.IntegerField(min_value=100)


class ActivatePromoSerializer(serializers.Serializer):
    promo = serializers.CharField(max_length=10)

