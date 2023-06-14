from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .resources import *
from .models import TicketMistake
from .models import *


class StaffAdmin(admin.ModelAdmin):
    model = Staff
    list_display = ['fullname', 'level', 'staff_number', 'username',]
    search_fields = ['fullname',]
    list_filter = ['team',]

#@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    model = Staff
    #resource_class = TicketResource
    list_display = ['ticket_id', 'ticket_type', 'service_type', 'creator', 'registration_date', 'creation_date', 'due_date', 'end_date', 'quality_date', 'configuer_name', 'config_date' ]
    search_fields = ['bcrm_id', 'rt_id', 'ticketing_id', 'ticket_id']
    list_filter = ['branch_type', 'status', 'qualiter', 'ticket_type', 'ticket_thread_name' ]
#    save_as = True


admin.site.register(TicketMistake)
admin.site.register(ColorAdjustment)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(ServiceType)
admin.site.register(Car)
admin.site.register(Channel)
admin.site.register(Warehouse)
admin.site.register(GponType)
admin.site.register(StbType)
admin.site.register(WifiRouter)
admin.site.register(OtherDevice)
admin.site.register(OpticalCable)
admin.site.register(LanCable)
admin.site.register(Muft)
admin.site.register(Spliter)
admin.site.register(TicketThread)
