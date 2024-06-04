from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view

from .serializers import (
    BalanceSerializer,
    PromocodeSerializer,
    ActivatePromoSerializer,
    CreatePromocodeSerializer,
)
from .models import Balance, Promocode
from .services import create_promocodes


@api_view(['GET', 'POST'])
def balance_view(request):
    if request.method == 'GET':
        qs = Balance.objects.get(pk=1)
        serializer = BalanceSerializer(qs)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass


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
