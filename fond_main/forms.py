from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from django.forms import Textarea, Select
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import *


class LogInForm(forms.Form):
    username    =   forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password    =   forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user_qs = User.objects.filter(username=username)
        if user_qs.count() == 0:
            raise forms.ValidationError("The user does not exist")
        else:
            if username and password:
                 user = authenticate(username=username, password=password)

                 if not user:
                    raise forms.ValidationError("Incorrect password")
                 if not user.is_active:
                     raise forms.ValidationError("This user is no longer active")
        return super(LogInForm,self).clean(*args,**kwargs)


class OpTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = '__all__'


class TechTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = '__all__'

class ConfTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = '__all__'


class DatePickerInput(forms.DateTimeInput):
    input_type = 'datetime-local'

QUALITY_STATUS_TYPE = (('Incomplete','Incomplete'), ('Solved', 'Solved'))


class CreateTicketForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateTicketForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Ticket
        fields = ['ticket_type', 'ticket_thread_name', 'bcrm_id',
            'rt_id', 'ticketing_id', 'branch_type', 'region', 'district',
            'address', 'registration_date', 'creation_date', 'tarif_id', 'service_type', 'service_quantity',
            'due_date', 'comment', 'performer', 'creator',
            'performer_group',  'status', ]
        widgets = {
                'due_date' : DatePickerInput(format ='%Y-%m-%d %H:%M', attrs=  {'class':'form-control'}),
                'registration_date' : DatePickerInput(format ='%Y-%m-%d %H:%M', attrs=  {'class':'form-control'}),
                }


class OPCustomForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('registration_date', 'ticket_type', 'ticket_thread_name', 'bcrm_id',
            'rt_id', 'ticketing_id', 'branch_type', 'region', 'district',
            'address', 'tarif_id', 'service_type', 'service_quantity',
            'due_date', 'comment', 'performer', 'creator',
            'performer_group', 'status', 'car_number', 'tower_working_time', 'current_or_capital', 'warehouse',
            'channel', 'gpon_type', 'gpon_qty', 'stb_type', 'stb_qty',
            'stb_2_type', 'stb_2_qty', 'stb_3_type', 'stb_3_qty',
            'wifi_router_type', 'wifi_router_qty', 'other_device_type',
            'other_device_qty', 'points', 'optical_cabel_type', 'optical_cable_length',
            'optical_cable_begin', 'optical_cable_end', 'optical_cable_code',
            'demontage_optical_cable_type', 'demontage_optical_cable_length',
            'defected_optical_cable_type', 'defected_optical_cable_length',
            'lan_cable_type', 'utp_cable_length', 'utp_cable_begin', 'utp_cable_end', 'utp_cable_code',
            'ftp_cable_length', 'ftp_cable_begin', 'ftp_cable_end', 'ftp_cable_code',
            'hdmi_qty', 'remote_control_qty', 'muft', 'muft_qty', 'spliter', 'spliter_qty',
            'muft_2', 'muft_2_qty', 'muft_3', 'muft_3_qty',
            'spliter_2', 'spliter_2_qty', 'spliter_3', 'spliter_3_qty',
            'technician1', 'technician2', 'technician3', 'technician4', 'technician5',
            'technician1_failed', 'technician2_failed', 'technician3_failed',
            'tech_comment', 'quality_status', 'quality_comment',
            'difficaulty', 'distance', 'tower', 'extra_work', 'state', 'worktime')

        widgets = {
                'tech_comment': Textarea(attrs={'cols': 0, 'rows': 6}),
                'due_date' : DatePickerInput(format ='%Y-%m-%dT%H:%M', attrs=  {'class':'form-control chosen-select', }),
                'registration_date' : DatePickerInput(format ='%Y-%m-%dT%H:%M', attrs=  {'class':'form-control chosen-select', }),
                }

    def __init__(self, *args, **kwargs):
        super(OPCustomForm, self).__init__(*args, **kwargs)
        self.fields['quality_status'] = forms.ChoiceField(choices=QUALITY_STATUS_TYPE)
        self.fields['quality_status'].required = False
        self.fields['quality_comment'].disabled = True
        if self.initial['status'] == 'Done' or self.initial['status'] == 'Reject':
            self.fields['status'].disabled = True


STATUS_TYPE = (('Waiting','Waiting'),('Pending','Pending'),('Config','Config'),('Done','Done'))

class TechCustomForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('status', 'car_number', 'tower_working_time', 'current_or_capital', 'warehouse',
            'channel', 'gpon_type', 'gpon_qty', 'stb_type', 'stb_qty',
            'stb_2_type', 'stb_2_qty', 'stb_3_type', 'stb_3_qty',
            'wifi_router_type', 'wifi_router_qty', 'other_device_type',
            'other_device_qty', 'points', 'optical_cabel_type', 'optical_cable_length',
            'optical_cable_begin', 'optical_cable_end', 'optical_cable_code',
            'demontage_optical_cable_type', 'demontage_optical_cable_length',
            'defected_optical_cable_type', 'defected_optical_cable_length',
            'lan_cable_type', 'utp_cable_length', 'utp_cable_begin', 'utp_cable_end', 'utp_cable_code',
            'ftp_cable_length', 'ftp_cable_begin', 'ftp_cable_end', 'ftp_cable_code',
            'hdmi_qty', 'remote_control_qty', 'muft', 'muft_qty', 'spliter', 'spliter_qty',
            'muft_2', 'muft_2_qty', 'muft_3', 'muft_3_qty',
            'spliter_2', 'spliter_2_qty', 'spliter_3', 'spliter_3_qty',
            'technician1', 'technician2', 'technician3', 'technician4', 'technician5',
            'technician1_failed', 'technician2_failed', 'technician3_failed', 'tech_comment',
            'quality_status', 'quality_comment', 'difficaulty', 'distance', 'tower',
            'extra_work' , 'state', 'worktime'
            )
        widgets  = { 
                'tech_comment': Textarea(attrs={'cols': 0, 'rows': 6}),
#                'status' : Select(choices=STATUS_TYPE, attrs={'class' : 'form-control'}),
                }

    def __init__(self, *args, **kwargs):
        super(TechCustomForm, self).__init__(*args, **kwargs)
        self.fields['quality_status'] = forms.ChoiceField(choices=QUALITY_STATUS_TYPE)
        self.fields['quality_status'].required = False
        self.fields['quality_comment'].disabled = True
        self.fields['status'] = forms.ChoiceField(choices=STATUS_TYPE)
        #self.fields['car_number'].required = True
        #self.fields['current_or_capital'].required = True
        #self.fields['points'].required = True
        #self.fields['channel'].required = True
        if self.initial['status'] == 'Done' or self.initial['status'] == 'Reject':
            self.fields['status'].disabled = True


class ConfCustomForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('status', 'configuer_name', 'trubka', 'color_adjustment', 'blm_clx', 'service_link_measure', 
                'tech_comment',)

        widgets  = { 'tech_comment': Textarea(attrs={'cols': 0, 'rows': 6}) }

    def __init__(self, *args, **kwargs):
        super(ConfCustomForm, self).__init__(*args, **kwargs)
        self.fields['status'] = forms.ChoiceField(choices=STATUS_TYPE)
        if self.initial['status'] == 'Done' or self.initial['status'] == 'Reject':
            self.fields['status'].disabled = True

class QualityCustomForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('ticket_type', 'ticket_thread_name', 'bcrm_id',
            'rt_id', 'ticketing_id', 'branch_type', 'region', 'district',
            'address', 'registration_date', 'creation_date', 'tarif_id', 'service_type', 'service_quantity',
            'due_date', 'comment', 'status', 'creator', 'performer', 'creation_date', 'end_date',
            'performer_group',   'configuer_name', 'trubka', 'config_date', 
            'color_adjustment', 'blm_clx', 'service_link_measure',
            'quality_mistake', 'quality_status', 'quality_comment', 'qualiter', 'mistake_author',
            'mistake_part',  )
        widgets = {
                'quality_comment': Textarea(attrs={'cols': 0, 'rows': 6}),
                'due_date' : DatePickerInput(format ='%Y-%m-%dT%H:%M', attrs=  {'class':'form-control chosen-select', }),
                'registration_date' : DatePickerInput(format ='%Y-%m-%dT%H:%M', attrs=  {'class':'form-control chosen-select', }),
                }

    def __init__(self, *args, **kwargs):
        super(QualityCustomForm, self).__init__(*args, **kwargs)
        self.fields['status'].disabled = True
        self.fields['creation_date'].disabled = True
        self.fields['performer'].disabled = True
        self.fields['creator'].disabled = True
        self.fields['configuer_name'].disabled = True
        self.fields['end_date'].disabled = True
        self.fields['config_date'].disabled = True

