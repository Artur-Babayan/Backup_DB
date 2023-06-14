from datetime import datetime, timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
        ordering = ['first_name', 'last_name' ]


    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

CAR_TYPE = (('Normal','Normal'),('Tower','Tower'))

class Car(models.Model):
    car_code = models.CharField(primary_key=True, max_length=255)
    car_name = models.CharField(max_length=255)
    car_type = models.CharField(max_length=60, choices=CAR_TYPE, blank=False, null=False, default='')

    class Meta:
        managed = True
        db_table = 'car'
        ordering = ['car_name', ]

    def __str__(self):
        return '{} {} {}'.format(self.car_name, self.car_code, self.car_type)


class Channel(models.Model):
    channel_code = models.IntegerField(primary_key=True)
    channel_name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'channel'
        ordering = ['channel_name', ]

    def __str__(self):
        return self.channel_name


class ColorAdjustment(models.Model):
    color_adjustment_name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'color_adjustment'
        ordering = ['color_adjustment_name', ]

    def __str__(self):
        return self.color_adjustment_name


class District(models.Model):
    district = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'district'
        ordering = ['district', ]

    def __str__(self):
        return self.district


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Staff(models.Model):
    division = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    position_en = models.CharField(max_length=255)
    position_type = models.CharField(max_length=255)
    group_type = models.CharField(max_length=255)
    staff_number = models.PositiveIntegerField(primary_key=True)
    fullname = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)
    position_am = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    username = models.ForeignKey(AuthUser, on_delete=models.CASCADE, db_column='username', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'staff'
        verbose_name_plural = 'Staff'
        ordering = ['fullname', ]

    def __str__(self):
        return self.fullname

class GponType(models.Model):
    gpon_type = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'gpon_type'
        ordering = ['gpon_type', ]

    def __str__(self):
        return self.gpon_type


class LanCable(models.Model):
    lan_cable_code = models.IntegerField(primary_key=True)
    lan_cable_name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'lan_cable'
        ordering = ['lan_cable_name', ]

    def __str__(self):
        return self.lan_cable_name


class OpticalCable(models.Model):
    optical_cable_code = models.IntegerField(primary_key=True)
    optical_cable_name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'optical_cable'
        ordering = ['optical_cable_name', ]

    def __str__(self):
        return self.optical_cable_name


class Region(models.Model):
    region = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'region'
        ordering = ['region', ]

    def __str__(self):
        return self.region


class ServiceType(models.Model):
    service_type = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'service_type'
        ordering = ['service_type', ]

    def __str__(self):
        return self.service_type


class StbType(models.Model):
    stb_name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'stb_type'
        ordering = ['stb_name', ]

    def __str__(self):
        return self.stb_name


class TicketThread(models.Model):
    ticket_thread = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'ticket_thread'
        ordering = ['ticket_thread', ]

    def __str__(self):
        return self.ticket_thread

class Warehouse(models.Model):
    warehouse = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'warehouse'
        ordering = ['warehouse', ]

    def __str__(self):
        return self.warehouse

class WifiRouter(models.Model):
    wifi_router_name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'wifi_router'
        ordering = ['wifi_router_name', ]

    def __str__(self):
        return self.wifi_router_name

class Spliter(models.Model):
    spliter_code = models.IntegerField(primary_key=True)
    spliter_name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'spliter'
        ordering = ['spliter_name', ]

    def __str__(self):
        return '{} {}'.format(self.spliter_code, self.spliter_name)

class Muft(models.Model):
    muft_code = models.IntegerField(primary_key=True)
    muft_name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'muft'
        ordering = ['muft_name', ]

    def __str__(self):
        return '{} {}'.format(self.muft_code, self.muft_name)

class OtherDevice(models.Model):
    other_device_name = models.CharField(max_length=255)
    other_device_code = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'other_device'
        ordering = ['other_device_name', ]

    def __str__(self):
        return '{} {}'.format(self.other_device_code, self.other_device_name)

class TicketMistake(models.Model):
    ticket_mistake_name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'ticket_mistake'
        ordering = ['ticket_mistake_name', ]
        verbose_name_plural = 'Ticket Mistake'

    def __str__(self):
        return self.ticket_mistake_name

TICKET_TYPE = (('Measuring', 'Measuring'), ('Servicing', 'Servicing'),
    ('Construction','Construction'), ('Welding','Welding'),
    ('Design','Design'), ('Connection','Connection'), ('Emergency','Emergency'))

BRANCH_TYPE = (('B2C','B2C'),('B2B','B2B'),('B2C PS','B2C PS'), ('Other', 'Other'))

STATUS_TYPE = (('Waiting','Waiting'),('Pending','Pending'),('Config','Config'),('Done','Done'),('Reject','Reject'))

CC_TYPE = (('',''),('Current','Current'),('Capital','Capital'))

MISTAKE_TYPE = (('',''),('Checked','Checked'),('Incomplete','Incomplete'),('Corrected','Corrected'), ('Solved','Solved'), ('Punishment','Punishment'))

MISTAKE_PART = (('Operational Part','Operational Part'),('Config Part','Config Part'),('Operational/Config Part','Operational/Config Part'), ('Technical Part','Technical Part'), ('Technician Part','Technician Part'), ('Technical/Technician Part', 'Technical/Technician Part'), ('Technical/Technician/Config Part', 'Technical/Technician/Config Part'), ('Technical/Technician/Operational Part' ,'Technical/Technician/OP Part'))

DISTANCE_TYPE = (('',''),('<30','<30'),('30-80','30-80'),('80-150','80-150'),('>150','>150'))

DIFF_TYPE = ((1, 1),(1.25, 1.25),(1.5, 1.5))

class Ticket(models.Model):
#   OPERATION LEVEL
    ticket_id = models.AutoField(primary_key=True)
    ticket_type = models.CharField(max_length=60, choices=TICKET_TYPE, default='')
    ticket_thread_name = models.ForeignKey(TicketThread, on_delete=models.CASCADE, related_name='ticket_thread_name', db_column='ticket_thread_name', blank=False, null=False)
    bcrm_id = models.PositiveIntegerField(blank=True, null=True)
    rt_id = models.PositiveIntegerField(blank=True, null=True)
    ticketing_id =models.PositiveIntegerField(blank=True, null=True)
    branch_type = models.CharField(max_length=60, choices=BRANCH_TYPE, blank=False, null=False, default='')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='ticket_region', db_column='region', blank=False, null=False)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='ticket_district',db_column='district', blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    registration_date = models.DateTimeField(blank=False, null=False)
    creation_date = models.DateTimeField(blank=True, null=True)
    tarif_id = models.CharField(max_length=255, blank=True, null=True)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='ticket_service', db_column='service_type', blank=False, null=False)
    service_quantity = models.PositiveIntegerField()
    due_date = models.DateTimeField(blank=False, null=False)
    comment = models.CharField(max_length=255, blank=True, null=True)
    performer = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='ticket_performer', db_column='performer', blank=False, null=False)
    creator = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='ticket_creator', db_column='creator', blank=False, null=False)  # hide in form
    performer_group = models.IntegerField(blank=True, null=True, choices=[(i,i) for i in range(21)])
    status = models.CharField(max_length=60, choices=STATUS_TYPE, blank=False, null=False, default='')
    deadline = models.DateTimeField(blank=True, null=True)
#-----------TECHNICAL LEVEL----------------------------
    car_number = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='ticket_car', db_column='car_number', blank=True, null=True)
    tower_working_time = models.PositiveIntegerField(blank=True, null=True)
    current_or_capital = models.CharField(max_length=60, choices=CC_TYPE, blank=True, null=True, default='')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='ticket_warehouse', db_column='warehouse', blank=True, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='ticket_channel', db_column='channel', blank=True, null=True)
    gpon_type = models.ForeignKey(GponType, on_delete=models.CASCADE, related_name='ticket_gpon', db_column='gpon_type', blank=True, null=True)
    gpon_qty = models.PositiveIntegerField(blank=True, null=True)
    stb_type = models.ForeignKey(StbType, on_delete=models.CASCADE, related_name='ticket_stb', db_column='stb_type', blank=True, null=True)
    stb_2_type = models.ForeignKey(StbType, on_delete=models.CASCADE, related_name='ticket_stb_2', db_column='stb_2_type', blank=True, null=True)
    stb_3_type = models.ForeignKey(StbType, on_delete=models.CASCADE, related_name='ticket_stb_3', db_column='stb_3_type', blank=True, null=True)
    stb_qty = models.PositiveIntegerField(blank=True, null=True)
    stb_2_qty = models.PositiveIntegerField(blank=True, null=True)
    stb_3_qty = models.PositiveIntegerField(blank=True, null=True)
    wifi_router_type = models.ForeignKey(WifiRouter, on_delete=models.CASCADE, related_name='ticket_wifi_router', db_column='wifi_router_type', blank=True, null=True)
    wifi_router_qty = models.PositiveIntegerField(blank=True, null=True)
    other_device_type = models.ForeignKey(OtherDevice, on_delete=models.CASCADE, related_name='ticket_other_device', db_column='other_device_type', blank=True, null=True)
    other_device_qty = models.PositiveIntegerField(blank=True, null=True)
    points = models.PositiveIntegerField(blank=True, null=True)
    optical_cabel_type = models.ForeignKey(OpticalCable, on_delete=models.CASCADE, related_name='ticket_optical_cabel', db_column='optical_cabel_type', blank=True, null=True)
    optical_cable_length = models.PositiveIntegerField(blank=True, null=True)
    optical_cable_begin = models.PositiveIntegerField(blank=True, null=True)
    optical_cable_end = models.PositiveIntegerField(blank=True, null=True)
    optical_cable_code = models.PositiveIntegerField(blank=True, null=True)
    demontage_optical_cable_type = models.ForeignKey(OpticalCable, on_delete=models.CASCADE, related_name='ticket_demon_opt_cabel', db_column='demontage_optical_cable_type', blank=True, null=True)
    demontage_optical_cable_length = models.PositiveIntegerField(blank=True, null=True)
    defected_optical_cable_type = models.ForeignKey(OpticalCable, on_delete=models.CASCADE, related_name='ticket_defect_opt_cabel', db_column='defected_optical_cable_type', blank=True, null=True)
    defected_optical_cable_length = models.PositiveIntegerField(blank=True, null=True)
    lan_cable_type = models.ForeignKey(LanCable, on_delete=models.CASCADE, related_name='ticket_lan_cabel', db_column='lan_cable_type', blank=True, null=True)
    utp_cable_length = models.PositiveIntegerField(blank=True, null=True)
    utp_cable_begin = models.PositiveIntegerField(blank=True, null=True)
    utp_cable_end = models.PositiveIntegerField(blank=True, null=True)
    utp_cable_code = models.PositiveIntegerField(blank=True, null=True)
    ftp_cable_length = models.PositiveIntegerField(blank=True, null=True)
    ftp_cable_begin = models.PositiveIntegerField(blank=True, null=True)
    ftp_cable_end = models.PositiveIntegerField(blank=True, null=True)
    ftp_cable_code = models.PositiveIntegerField(blank=True, null=True)
    hdmi_qty = models.PositiveIntegerField(blank=True, null=True)
    remote_control_qty = models.PositiveIntegerField(blank=True, null=True)
    muft = models.ForeignKey(Muft, on_delete=models.CASCADE, related_name='ticket_must', db_column='ticket_muft', blank=True, null=True)
    muft_qty = models.PositiveIntegerField(blank=True, null=True)
    muft_2 = models.ForeignKey(Muft, on_delete=models.CASCADE, related_name='ticket_muft_2', db_column='ticket_muft_2', blank=True, null=True)
    muft_2_qty = models.PositiveIntegerField(blank=True, null=True)
    muft_3 = models.ForeignKey(Muft, on_delete=models.CASCADE, related_name='ticket_muft_3', db_column='ticket_muft_3', blank=True, null=True)
    muft_3_qty = models.PositiveIntegerField(blank=True, null=True)
    spliter = models.ForeignKey(Spliter, on_delete=models.CASCADE, related_name='ticket_spliter', db_column='spliter', blank=True, null=True)
    spliter_qty = models.PositiveIntegerField(blank=True, null=True)
    spliter_2 = models.ForeignKey(Spliter, on_delete=models.CASCADE, related_name='ticket_spliter_2', db_column='spliter_2', blank=True, null=True)
    spliter_2_qty = models.PositiveIntegerField(blank=True, null=True)
    spliter_3 = models.ForeignKey(Spliter, on_delete=models.CASCADE, related_name='ticket_spliter_3', db_column='spliter_3', blank=True, null=True)
    spliter_3_qty = models.PositiveIntegerField(blank=True, null=True)
    technician1 = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='ticket_technician1', db_column='technician1', blank=True, null=True)
    technician2 = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='ticket_technician2', db_column='technician2', blank=True, null=True)
    technician3 = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='ticket_technician3', db_column='technician3', blank=True, null=True)
    technician4 = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='ticket_technician4', db_column='technician4', blank=True, null=True)
    technician5 = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='ticket_technician5', db_column='technician5', blank=True, null=True)
    technician1_failed = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='ticket_technician1_failed', db_column='technician1_failed', blank=True, null=True)
    technician2_failed = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='ticket_technician2_failed', db_column='technician2_failed', blank=True, null=True)
    technician3_failed = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='ticket_technician3_failed', db_column='technician3_failed', blank=True, null=True)
    tech_comment = models.CharField(max_length=255, blank=True, null=True)
#   CONFIG LEVEL
    config_date = models.DateTimeField(blank=True, null=True)
    configuer_name = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='ticket_conf_name', db_column='configuer_name', blank=True, null=True)
    trubka = models.IntegerField(blank=True, null=True, choices=[(i,i) for i in range(-1, 11)])
    color_adjustment = models.ForeignKey(ColorAdjustment, on_delete=models.CASCADE, related_name='ticket_color_adj',  db_column='color_adjustment', blank=True, null=True)
    blm_clx = models.CharField(max_length=255, blank=True, null=True)
    service_link_measure = models.CharField(max_length=255, blank=True, null=True)
#   QUALITY LEVEL
    quality_mistake = models.ForeignKey(TicketMistake, on_delete=models.CASCADE, related_name='ticket_quality_mistake',  db_column='quality_mistake', blank=True, null=True)
    quality_status = models.CharField(max_length=60, choices=MISTAKE_TYPE, default='', blank=True, null=True)
    quality_date = models.DateTimeField(blank=True, null=True)
    quality_deadline = models.DateTimeField(blank=True, null=True)
    quality_comment = models.CharField(max_length=555, blank=True, null=True, default='')
    qualiter = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='ticket_qualiter', db_column='qualiter', blank=True, null=True)
    mistake_author = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='ticket_mistake_author', db_column='mistake_author', blank=True, null=True)
    mistake_part = models.CharField(max_length=60, choices=MISTAKE_PART, default='', blank=True, null=True)
#   END FIELD
    end_date = models.DateTimeField(blank=True, null=True) #hide in form
#   NEW FIELD 01.05
    difficaulty = models.FloatField(choices=DIFF_TYPE, default=1.0, blank=True, null=True)
    distance = models.CharField(max_length=60, choices=DISTANCE_TYPE, default='', blank=True, null=True)
    tower = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='ticket_tower', db_column='tower', blank=True, null=True)
#   NEW FIELD 01.06 (TCC)
    extra_work = models.CharField(max_length=60, choices=(('',''),('Overtime','Overtime'), ('Weekend','Weekend')), default='', blank=True, null=True)
    state = models.CharField(max_length=60, choices=(('',''),('Region','Region')), default='', blank=True, null=True)
    worktime = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ticket'
        verbose_name_plural = 'Ticket'

    def __str__(self):
        return '{} / {} / {}'.format(self.ticket_id, self.ticket_thread_name, self.ticket_type)

    def save(self, *args, **kwargs):
        if self.status == 'Config':
            self.config_date = datetime.now()
        elif self.status == 'Done' or self.status == 'Reject':
            if not self.quality_status == '':
                self.quality_date = datetime.now()
                self.quality_deadline = datetime.now() + timedelta(3)
            else:
                if not self.creation_date :
                    self.creation_date = datetime.now()
                else:
                    if not self.end_date:
                        self.end_date = datetime.now()
        else:
            if not self.creation_date :
                self.creation_date = datetime.now()
        #if not self.quality_status == '':
        #    self.quality_date = datetime.now()
        #    self.quality_deadline = datetime.now() + timedelta(3) 
        super(Ticket, self).save(*args, **kwargs)


    def clean(self, *args, **kwargs):
        reg_handle_time = timezone.now() - timedelta(days=720)
        due_handle_time = timezone.now() + timedelta(days=360)
        super(Ticket, self).clean(*args, **kwargs)
        if self.registration_date < reg_handle_time:
            raise ValidationError("Registration Date must not be earlier than 720 days from today!")
        elif self.due_date > due_handle_time: # or self.due_date < self.registration_date:
            raise ValidationError('Due Date must not exceed 360 days from today and earlier than registration date!')
#        elif self.quality_status in ['Punishment',  'Corrected']:
#            raise ValidationError('You cant edit ticket when its have Punishment, Checked or Correted quality status!')

