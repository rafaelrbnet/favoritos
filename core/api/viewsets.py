from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from core.models import Favoritos
from .serializers import FavoritosSerializer


class FavoritosViewSet(ModelViewSet):
    queryset = Favoritos.objects.all()
    serializer_class = FavoritosSerializer
    permission_classes = (DjangoModelPermissions,)  # herança do modulo de permissão do admin
    authentication_classes = (TokenAuthentication,)
