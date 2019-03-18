from rest_framework import serializers

from appcore.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = '__all__'

    @staticmethod
    def get_status(ticket):
        return ticket.get_status()

    @staticmethod
    def get_user(ticket):
        username = None
        try:
            username = ticket.user.username
        except Exception:
            pass
        return (username is None) and 'Usuario no asignado' or username
