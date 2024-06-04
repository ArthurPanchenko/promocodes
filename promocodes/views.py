from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view

from .serializers import (
    BalanceSerializer,
    PromocodeSerializer,
    ActivatePromoSerializer,
    CreatePromocodeSerializer,
)
from .models import Balance, Promocode
from .services import create_promocodes


class BalanceDetail(RetrieveAPIView):
    
    def get_object(self):
        return Balance.objects.get(pk=1)
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BalanceSerializer
        elif self.request.method == 'POST':
            return ActivatePromoSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        balance = Balance.objects.get(pk=1)
        promocode = Promocode.objects.get(code=serializer.data['promo'])
        balance.balance += promocode.amount
        balance.save()
        Promocode.objects.get(pk=promocode.pk).delete()
        return Response({'status': 'activated'})


class PromocodeList(ListAPIView):
    queryset = Promocode.objects.all()[:5]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PromocodeSerializer
        elif self.request.method == 'POST':
            return CreatePromocodeSerializer
            
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        created_promocodes = create_promocodes(data['count'], data['prefix'], data['amount'])
        get_serializer = PromocodeSerializer(created_promocodes, many=True)
        return Response(get_serializer.data)
