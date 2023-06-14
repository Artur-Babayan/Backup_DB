from import_export import resources
from .models import *


class TicketResource(resources.ModelResource):

    class Meta:
        model = Ticket
        import_id_fields = ('ticket_id', )
        #exclude = ('id',)
        fields = [field.name for field in Ticket._meta.get_fields()]

