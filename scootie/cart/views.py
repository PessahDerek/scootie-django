from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Cart, Client, CartItem
from bikes.models import Bike
from .serializers import CartSerializer, ClientSerializer


# Create your views here.
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    model = Cart
    serializer_class = CartSerializer

    # @action(methods=['POST'], detail=False, name="send-email", url_path="")
    def create(self, request, *args, **kwargs):
        items = []
        for item in request.data['items']:
            try:
                bike = Bike.objects.get(id=item['id'])
                new_item = CartItem.objects.create(
                    brand=item['brand'], model=item['model'],
                    price=bike.price, discount=bike.discount,
                    qty=item['qty'], bike_id=bike.id
                )
                items.append(new_item.id)
            except Exception as e:
                print(e)
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        try:
            found_client = Client.objects.get(phone=request.data['client']['phone'])
        except Client.DoesNotExist:
            found_client = Client.objects.create(
                phone=request.data['client']['phone'], first_name=request.data['client']['first_name'],
                last_name=request.data['client']['last_name'], email=request.data['client']['email']
            )
        request.data['client'] = found_client.id
        request.data['items'] = items
        print("id: ", request.data['client'])
        new_cart_item = super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    model = Client
    serializer_class = ClientSerializer
