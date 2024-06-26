from rest_framework import viewsets
from inventApp.models import Proudcto
from inventApp.api.serializer import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Proudcto.objects.all()
    serializer_class = ProductoSerializer