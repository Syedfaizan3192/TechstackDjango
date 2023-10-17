from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

from ..models import Product


def success_response(data, message, status_code=200, send_data=True):
    response = {
        'success': True,
        'message': message,
    }
    if send_data:
        response['data'] = data
    return Response(response, status=status_code)


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'price']
    search_fields = ['name', 'description']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return success_response(serializer.data, 'Products retrieved successfully')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(serializer.data, 'Product created successfully',
                                    status_code=status.HTTP_201_CREATED)
        return success_response(serializer.errors, 'Invalid input data', status_code=status.HTTP_400_BAD_REQUEST)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return success_response(serializer.data, 'Product retrieved successfully')

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return success_response(serializer.data, 'Product updated successfully')
        return success_response(serializer.errors, 'Invalid input data', status_code=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return success_response(None, 'Product deleted successfully', status_code=status.HTTP_204_NO_CONTENT)


__all__ = ['ProductList', 'ProductDetail']
