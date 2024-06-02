from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BalanceSerializer
from .models import Balance


@api_view()
def index(request):
    qs = Balance.objects.get(pk=1)
    serializer = BalanceSerializer(qs)
    return Response(serializer.data)