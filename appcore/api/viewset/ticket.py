from rest_framework.viewsets import ModelViewSet

from appcore.api.serializer.ticket import TicketSerializer
from appcore.models import Ticket


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
