from django.http import JsonResponse
from rest_framework import generics, mixins, permissions

from ..models import Organization, Product
from ..serializers.products import ProductSerializer

# This will be only for create (POST)
# class ProductCreateAPIView(generics.CreateAPIView):

# This will handel GET and POST requests
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    """"
        perform_create will be called only if it's under generics.CreateAPIView
        the following method will be called only if it's a POST request
    """
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print('--> perform_create <--')
       
        print(serializer.validated_data)
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name

        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # loopup_field = 'pk'


# Will not use this method because we can use ListCreateAPIView at the same time
# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # loopup_field = 'pk'
    
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    loopup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.name

product_update_view = ProductUpdateAPIView.as_view()



class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    loopup_field = 'pk'

    def perform_destroy(self, instance):
        super().perfrom_destroy(instance)

product_delete_view = ProductDestroyAPIView.as_view()