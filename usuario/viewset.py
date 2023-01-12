from rest_framework import viewsets

from .serializers import UserSerializer
from django.contrib.auth.models import User

class PedidosViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer