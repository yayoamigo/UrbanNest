from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import House
from .serializers import HouseSerializer

class HouseList(APIView):
    def get(self, request, format=None):
        houses = House.objects.all()
        serializer = HouseSerializer(houses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class HouseDetail(APIView):
    def get_obejct(self, pk):
        try:
            return House.objects.get(pk=pk)
        except House.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self, request, pk, format=None):
        house = self.get_obejct(pk)
        serializer = HouseSerializer(house)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        house = self.get_obejct(pk)
        serializer = HouseSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)