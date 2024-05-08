from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer

@api_view(['GET', 'POST'])
def account_list(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def account_detail(request, pk):
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_destination(request, account_id):
    try:
        account = Account.objects.get(pk=account_id)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = DestinationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(account=account)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_destinations(request, account_id):
    try:
        account = Account.objects.get(pk=account_id)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    destinations = Destination.objects.filter(account=account)
    serializer = DestinationSerializer(destinations, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def receive_data(request):
    app_secret_token = request.headers.get('app_secret_token')
    if not app_secret_token:
        return Response({'error': 'App secret token is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        account = Account.objects.get(app_secret_token=app_secret_token)
    except Account.DoesNotExist:
        return Response({'error': 'Invalid app secret token'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({'message': 'Data received and processed successfully'}, status=status.HTTP_200_OK)