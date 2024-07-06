from os.path import join

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.mail import send_mail

from bikes.models import Bike
from scootie import settings


class CartViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        pass

    def create(self, request, *args, **kwargs):
        try:
            print(request.data)
            client = request.data['client']
            items = []
            for item in request.data['items']:
                try:
                    found = Bike.objects.get(id=item['id'])
                    subtotal = item['qty']*(found.discount if found.discount > 0 else found.price)
                    items.append(
                        {'brand': found.brand, 'model': found.model, 'price': found.price, 'discount': found.discount,
                         "qty": item['qty'], 'subtotal': subtotal})
                except Bike.DoesNotExist:
                    continue
            # html = ""
            # with open(join(settings.BASE_DIR, 'templates', 'order.html')) as f:
            #     html = f.read()
            # html = join(settings.BASE_DIR, 'templates', 'order.html')
            # html_out = render_to_string('scootie', {'client': client, 'items': items}),
            send_mail(
                subject="Order received",
                # html_message=html_out,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER, client['email']],
                fail_silently=False,
                message="wtf"
            )
        except Exception as e:
            print("Fuck: ", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'welp'}, status=status.HTTP_201_CREATED)

    # Function to send confirmation email with cart details (implementation required)
    def send_cart_confirmation_email(self, cart):
        # Implement logic to send email with cart details like customer info,
        # item details (brand, model, price, discount, quantity) and total cost
        pass
