from rest_framework.serializers import ModelSerializer
from produto.models import Produto


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ('preco', 'imagem', 'marca', 'codigo', 'titulo', 'avaliacoes')
