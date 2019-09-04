from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from cliente.models import Cliente
from .serializers import ClienteSerializer


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = (DjangoModelPermissions,)  # herança do modulo de permissão do admin
    authentication_classes = (TokenAuthentication,)

