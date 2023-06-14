from django import forms
from django.db.models import Q
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
import django_filters

from .models import *


class TicketFilter(django_filters.FilterSet):
    
    filter_id = django_filters.CharFilter(method='id_filter', label='ID', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'ID'}))
    end_date = django_filters.CharFilter(label='End Date', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'example 2022-05-26'}))
    creation_date = django_filters.CharFilter(label='Creation Date', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'ex.2022-05-26'}))
    due_date = django_filters.CharFilter(label='Due Date', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'ex.2022-05-26'}))
    address = django_filters.CharFilter(label='Address', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': ''}))
    tarif_id = django_filters.CharFilter(label='Tarif ID', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': ''}))
    comment = django_filters.CharFilter(label='Comment', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': ''}))

    class Meta:
        model = Ticket
        fields = ['filter_id', 'ticket_thread_name', 'service_type', 'status', 'end_date', 'creation_date', 
                'district', 'address', 'tarif_id', 'due_date',
                'performer',  'deadline', 'comment', 'branch_type', ]

    def __init__(self, *args, **kwargs):
        super(TicketFilter, self).__init__(*args, **kwargs)

    def id_filter(self, queryset, name, value):
        return queryset.filter(
            Q(bcrm_id__icontains=value) | Q(rt_id__icontains=value) | Q(ticketing_id__icontains=value) )

    def comment_filter(self, queryset, name, value):
        return queryset.filter(
            Q(comment__icontains=value) | Q(tech_comment__icontains=value))

#--------------------------------------------- Quality Filter ---------------------------------------------

class QualityTicketFilter(django_filters.FilterSet):

    filter_id = django_filters.CharFilter(method='id_filter', label='ID', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'ID'}))
    end_date = django_filters.CharFilter(label='End Date', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'example 2022-05-26'}))
    creation_date = django_filters.CharFilter(label='Creation Date', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'ex.2022-05-26'}))
    quality_date = django_filters.CharFilter(label='Quality Date', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'ex.2022-05-26'}))
    quality_deadline = django_filters.CharFilter(label='Quality Deadline', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'ex.2022-05-26'}))
    address = django_filters.CharFilter(label='Address', lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': ''}))

    class Meta:
        model = Ticket
        fields = ['filter_id', 'ticket_thread_name', 'service_type', 'quality_status', 'quality_mistake',
                'qualiter', 'district', 'address', 'creation_date', 'end_date',
                'quality_date',  'quality_deadline', 'quality_comment', 'branch_type', ]

    def __init__(self, *args, **kwargs):
        super(QualityTicketFilter, self).__init__(*args, **kwargs)

    def id_filter(self, queryset, name, value):
        return queryset.filter(
            Q(bcrm_id__icontains=value) | Q(rt_id__icontains=value) | Q(ticketing_id__icontains=value) )


#--------------------------------------------- Other Filter   ---------------------------------------------

class OPTicketFilter(django_filters.FilterSet):
    class Meta:
        model = Ticket
        fields = ['ticket_id', 'ticket_thread_name', 'service_type', 'status', 'end_date', 'creation_date',
                'district', 'address', 'tarif_id', 'due_date',
                'performer', 'comment', 'branch_type', ]


class TechTicketFilter(django_filters.FilterSet):
    class Meta:
        model = Ticket
        fields = ['ticket_thread_name', 'bcrm_id', 'rt_id', 'ticketing_id', 'status', 'branch_type', 'district', 
                'address', 'creation_date', 'tarif_id', 'service_type', 'end_date',  ]



