from rest_framework.viewsets import ModelViewSet

from core.models import Livro
from core.serializers import LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.order_by("-quantidade")
    serializer_class = LivroSerializer