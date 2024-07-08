from django.core.mail import send_mail
from django.template.loader import get_template
from rest_framework import viewsets, status
from rest_framework.response import Response

from bikes.models import Bike
from scootie import settings
from .models import Cart
from .serializers import CartSerializer


# from .serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        pass

    def create(self, request, *args, **kwargs):
        try:
            # Find/create customer customer = Customer.objects.get_or_create(email=request.data['client']['email'],
            # defaults=request.data['client']) create cart new_cart = Cart.objects.create(customer=customer[0])
            client = request.data['client']
            items = []
            cart_item_instances = []
            for item in request.data['items']:
                try:
                    found = Bike.objects.get(id=item['id'])
                    subtotal = item['qty'] * (found.discount if found.discount > 0 else found.price)
                    modified_item = {
                        'brand': found.brand,
                        'model': found.model,
                        'price': found.price,
                        'discount': found.discount,
                        # 'cart': new_cart,
                        "qty": item['qty'],
                        'subtotal': subtotal,
                        "id": item['id']
                    }
                    items.append(modified_item)
                    # new_cart_item = CartItem.objects.create(**modified_item)
                    # # new_cart_item.save()
                    # cart_item_instances.append(new_cart_item)
                except Bike.DoesNotExist:
                    continue
            self.send_cart_confirmation_email(self, client, items)
            # print("Items: ", cart_item_instances)
            # new_cart.items.bulk_create(cart_item_instances)
            # new_cart.save()
            # print("Created cart items: ", )
        except Exception as e:
            return Response({'error': "Sorry, we were unable to send the email, kindly refresh and try again!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Order has been successfully received, a copy has been sent to your email! '
                                    'Thank you for shopping with us.'}, status=status.HTTP_201_CREATED)

    # Function to send confirmation email with cart details (implementation required)
    @staticmethod
    def send_cart_confirmation_email(self, client, items):
        html_ = get_template('order.html').render({"client": client, "items": items})
        send_mail(
            subject="Order received",
            html_message=html_,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER, client['email']],
            fail_silently=False,
            message=html_
        )
