from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from appcore.api.serializer.ticket import TicketSerializer
from appcore.models import Ticket


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        title = str(data.get('title'))
        description = str(data.get('description'))
        user_id = str(data.get('user_id'))

        serializer = dict()
        headers = dict()

        try:
            ticket = Ticket()
            ticket.title = title
            ticket.description = description
            ticket.user_id = user_id
            ticket.save()
            serializer = self.serializer_class(ticket)
            headers = self.get_success_headers(serializer.data)
        except Exception:
            pass

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
