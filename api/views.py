import csv
import io
from datetime import datetime

from django.db.models import Sum, Count
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from api.serializers import DealFileSerializer, ClientsSerializer
from api.models import Deal


class DealFileUploadAPIView(generics.CreateAPIView):
    serializer_class = DealFileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)
        next(reader)
        for row in reader:
            Deal.objects.create(
                username=row[0],
                item=row[1],
                total=int(row[2]),
                quantity=int(row[3]),
                date=datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S.%f'),
            )
        
        return Response(status=status.HTTP_200_OK)


class ClientReturnAPIView(generics.ListAPIView):
    serializer_class = ClientsSerializer

    def get_queryset(self, *args, **kwargs):
        deals = Deal.objects.values('username').annotate(spent_money=Sum('total')).order_by('-spent_money')[:5]
        usernames_of_deal = deals.values_list('username', flat=True)
        usernames_items =  Deal.objects.filter(username__in=usernames_of_deal).values('username', 'item').annotate(count=Count('item')).order_by('username')
        items_list = [item['item'] for item in usernames_items]

        final_items = {}
        for item in usernames_items:
            if item['username'] not in final_items:
                if items_list.count(item['item']) >= 2:
                    final_items[item['username']] = [item['item']]
            else:
                if items_list.count(item['item']) >= 2:
                    final_items[item['username']].append(item['item'])

        for deal in deals:
            deal['gems'] = final_items[deal['username']]

        return deals
