from .models import Pedidos
from django.db.models import Q
from .serializers import PedidosSerializer

from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework import permissions

class PedidosConsumer(ListModelMixin, GenericAsyncAPIConsumer):

    queryset = Pedidos.objects.filter(Q(status_do_pedido='pendente') | Q(status_do_pedido='preparando'))
    serializer_class = PedidosSerializer
    permissions_class = [permissions.AllowAny]

    async def connect(self, **kwargs):
        await self.model_change.subscribe()
        await super().connect()


    @model_observer(Pedidos)
    async def model_change(self, message, observer:None, **kwargs):
        await self.send_json(message)

    @model_change.serializer
    def model_serializer(self, instance, action, **kwargs):
        return dict(data=PedidosSerializer(instance=instance).data, action=action.value)

