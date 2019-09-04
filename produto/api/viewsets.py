from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from produto.models import Produto
from .serializers import ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = (DjangoModelPermissions,)  # herança do modulo de permissão do admin
    authentication_classes = (TokenAuthentication,)

