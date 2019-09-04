from rest_framework.serializers import ModelSerializer
from core.models import Favoritos


class FavoritosSerializer(ModelSerializer):
    class Meta:
        model = Favoritos
        fields = ('cliente', 'produto')
