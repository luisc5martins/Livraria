from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import CharField, ModelSerializer
from core.models import Compra


class CompraSerializer(ModelSerializer):
    usuario = CharField(source="user.email", read_only=True)
    class Meta:
        model = Compra
        fields = "__all__"