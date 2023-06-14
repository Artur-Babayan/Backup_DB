from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, View
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.contrib.auth import logout as django_logout
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django_filters.views import BaseFilterView
from django_filters.views import FilterView

from .forms import *
from .models import *
from .filters import *
from .user_perm import *

from datetime import datetime, timedelta, date

config_level_threads = [ 'Service Creation request',
'Service Additional request','Service Point Creation Request 1',
'Service Point Creation Request 2', 'Cabling apartments',
'House cabling request', 'Corporate cabling request',
'Welding apartments', 'Corporate welding request',
'Corporate project', 'FON Planning Department',
'Service Creation Missing request', 'Service creation corporate customer issue',
'Service creation customer issue', 'Service creation welding issue',
'Service missing configuration', 'Service creation canceled application',
]

def user_login(request, template_name='login.html'): #Login
    login_form = LogInForm()
    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.user.groups.filter(name='Quality Group').exists():
                    return redirect('my_quality_ticket')
                else:
                    return redirect('all_ticket')
            else:
                return HttpResponse("Your account are closed: {0}, {1}".format(username, password))
        else:
            return render(request,template_name, {
                'error_message': ' Login Failed! Enter the username and password correctly. ', 'login_form': login_form })
            login(request, user)
            return redirect('http://fond.ucom.am/admin')
    return render(request, template_name, {'login_form': login_form})

def logout(request): # Logouts
    django_logout(request)
    return redirect('user-login')

#---------------------- Filtered View --------------------------------------


#---------------------- Ticket View ----------------------------------------
last_month = datetime.now() - timedelta(days=30)

class AllTicketView(BaseFilterView, ListView):
    model = Ticket
    template_name = 'all_index.html'
    filterset_class = TicketFilter
    ordering = ['creation_date']
    paginate_by = 200
    context_object_name = 'ticket_list'

    def get_queryset(self):
        if self.request.user.groups.filter(name='All Levels').exists():
            return Ticket.objects.all().order_by('-creation_date')
        elif self.request.user.groups.filter(name='Technical Level').exists():
            return Ticket.objects.filter(performer=self.request.user.id).exclude(status='Waiting').exclude( Q(status__in=['Done', 'Reject']) & Q(end_date__lte=date(2023, 2, 28)) ).order_by('-creation_date')
        elif self.request.user.groups.filter(name='Quality Group').exists():
            return Ticket.objects.all().order_by('-creation_date')
        elif self.request.user.groups.filter(name='Operational Level').exists():
            return Ticket.objects.filter( Q(creator=self.request.user.id) | Q(performer=self.request.user.id)).exclude( Q(status__in=['Done', 'Reject']) & Q(end_date__lte=date(2023, 2, 28)) ).order_by('-creation_date')
        elif self.request.user.groups.filter(name='Config Level').exists():
            return Ticket.objects.filter( Q(status__in=['Config', 'Done']) & Q(configuer_name__isnull=True) & Q(ticket_type='Connection') & Q(ticket_thread_name__in=['Service Additional request', 'Service Creation request'])).exclude( Q(status__in=['Done', 'Reject']) & Q(end_date__lte=date(2023, 2, 28)) ).order_by('-creation_date')
        else :
            return redirect('user-login')

    def get_context_data(self, **kwargs):
        context = super(AllTicketView, self).get_context_data(**kwargs)
        list_news = TicketFilter(self.request.GET, queryset=Ticket.objects.get_queryset().order_by('creation_date')).qs
        context['done_count'] = list_news.filter(status='Done').count()
        context['wait_count'] = list_news.filter(status='Waiting').count()
        context['pend_count'] = list_news.filter(status='Pending').count()
        context['conf_count'] = list_news.filter(status='Config').count()
        context['rej_count'] = list_news.filter(status='Reject').count()
        context['all_count'] = list_news.count()
        paginator = Paginator(list_news, 200)
        page = self.request.GET.get('page')
        try:
            news_paginate = paginator.page(page)
        except PageNotAnInteger:
            news_paginate = paginator.page(1)
        except EmptyPage:
            news_paginate = paginator.page(paginator.num_pages)
        context['qs'] = news_paginate
        return context


class TeamTicketView(BaseFilterView, ListView):
    model = Ticket
    template_name = 'team_ticket.html'
    filterset_class = TicketFilter
    ordering = ['creation_date']
    paginate_by = 200
    context_object_name = 'ticket_list'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Connection Group').exists():
            return Ticket.objects.filter(ticket_type='Connection').filter(status__in=['Waiting', 'Pending', 'Config']).exclude( Q(status__in=['Done', 'Reject']) & Q(end_date__lte=date(2023, 2, 28)) ).order_by('-creation_date')
        elif self.request.user.groups.filter(name='Quality Group').exists():
            return Ticket.objects.filter(qualiter__isnull=True).filter(status__in=['Done', 'Reject'])
        elif self.request.user.groups.filter(name='Construction Group').exists():
            return Ticket.objects.filter(ticket_type='Construction').filter(status__in=['Waiting', 'Pending']).exclude( Q(status__in=['Done', 'Reject']) & Q(end_date__lte=date(2023, 2, 28)) ).order_by('-creation_date')
        elif self.request.user.groups.filter(name='Emergency Group').exists():
            return Ticket.objects.filter(ticket_type='Emergency').filter(status__in=['Waiting', 'Pending']).exclude( Q(status__in=['Done', 'Reject']) & Q(end_date__lte=date(2023, 2, 28)) ).order_by('-creation_date')
        elif self.request.user.groups.filter(name='Servicing Group').exists():
            return Ticket.objects.filter(ticket_type='Servicing').filter(status__in=['Waiting', 'Pending']).exclude( Q(status__in=['Done', 'Reject']) & Q(end_date__lte=date(2023, 2, 28)) ).order_by('-creation_date')
        elif self.request.user.groups.filter(name='Welding Group').exists():
            return Ticket.objects.filter(ticket_type='Welding').filter(status__in=['Waiting', 'Pending']).exclude( Q(status__in=['Done', 'Reject']) & Q(end_date__lte=date(2023, 2, 28)) ).order_by('-creation_date')
        elif self.request.user.groups.filter(name='Deinstallation Group').exists():
            return Ticket.objects.filter(ticket_type='Servicing').filter(status__in=['Waiting', 'Pending'])\
                    .filter(ticket_thread_name__in=['Hardware Deinstallation', 'Lost Devices', 'DC Equipment Deinstallation'])\
                    .exclude( Q(status__in=['Done', 'Reject']) & Q(end_date__lte=date(2023, 2, 28)) ).order_by('-creation_date')
        else :
            return redirect('user-login')

    def get_context_data(self, **kwargs):
        context = super(TeamTicketView, self).get_context_data(**kwargs)
        list_news = TicketFilter(self.request.GET, queryset=Ticket.objects.get_queryset().order_by('creation_date')).qs
        context['done_count'] = list_news.filter(status='Done').count()
        context['wait_count'] = list_news.filter(status='Waiting').count()
        context['pend_count'] = list_news.filter(status='Pending').count()
        context['rej_count'] = list_news.filter(status='Reject').count()
        context['conf_count'] = list_news.filter(status='Config').count()
        context['all_count'] = list_news.count()
        paginator = Paginator(list_news, 200)
        page = self.request.GET.get('page')
        try:
            news_paginate = paginator.page(page)
        except PageNotAnInteger:
            news_paginate = paginator.page(1)
        except EmptyPage:
            news_paginate = paginator.page(paginator.num_pages)
        context['qs'] = news_paginate
        return context


class QualityTicketView(BaseFilterView, ListView):
    model = Ticket
    template_name = 'quality_ticket.html'
    filterset_class = QualityTicketFilter
    ordering = ['creation_date']
    paginate_by = 200
    context_object_name = 'ticket_list'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Quality Group').exists():
            return Ticket.objects.filter(qualiter=self.request.user.id).order_by('-creation_date')
        else:
            return Ticket.objects.filter(mistake_author=self.request.user.id).filter(quality_status__in=['Incomplete', 'Solved', 'Punishment', 'Corrected']).order_by('-creation_date')

    def get_context_data(self, **kwargs):
        context = super(QualityTicketView, self).get_context_data(**kwargs)
        list_news = QualityTicketFilter(self.request.GET, queryset=Ticket.objects.get_queryset().order_by('creation_date')).qs
        context['done_count'] = list_news.filter(status='Done').count()
        context['wait_count'] = list_news.filter(status='Waiting').count()
        context['pend_count'] = list_news.filter(status='Pending').count()
        context['rej_count'] = list_news.filter(status='Reject').count()
        context['conf_count'] = list_news.filter(status='Config').count()
        context['all_count'] = list_news.count()
        paginator = Paginator(list_news, 200)
        page = self.request.GET.get('page')
        try:
            news_paginate = paginator.page(page)
        except PageNotAnInteger:
            news_paginate = paginator.page(1)
        except EmptyPage:
            news_paginate = paginator.page(paginator.num_pages)
        context['qs'] = news_paginate
        return context


#---------------------------------------------------------------------------------------------------------------------------------------
class OperationalTicketView(FilterView):
    model = Ticket
    template_name = 'op_index.html'
    filterset_class = TicketFilter

    def get_queryset(self):
        return Ticket.objects.filter(creator=self.request.user.id)

class TechnicalTicketView(FilterView):
    model = Ticket
    template_name = 'tech_index.html'
    filterset_class = TicketFilter

    def get_queryset(self):
        qs1 = Q(performer=self.request.user.id)
        qs2 = Q(status='Pending')
        return Ticket.objects.filter(qs1 & qs2)


class ConfTicketView(FilterView):
    model = Ticket
    template_name = 'conf_index.html'
    filterset_class = TicketFilter

    def get_queryset(self):
        return Ticket.objects.filter(status='Config')


#-------------------------------- Ticket Detail ---------------------------


class TicketDetailView(View):
    def get(self, request, *args, **kwargs):
        ticket = get_object_or_404(Ticket, pk=kwargs['pk'])
        context = {'ticket': ticket}
        return render(request, 'ticket_detail.html', context)

#-------------------------------- Ticket Create ---------------------------

class TicketCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': CreateTicketForm()}
        return render(request, 'ticket_create.html', context)
    # --------- Davoyi gracna ---------

    # def post(self, request, *args, **kwargs):
    #     form = CreateTicketForm(request.POST)
    #     if form.is_valid():
    #         book = form.save()
    #         book.save()
    #         return redirect('all_ticket')
    #         #return HttpResponseRedirect(reverse_lazy('ticket_detail', args=[book.id]))
    #     return render(request, 'ticket_create.html', {'form': form})

    #------------ Arturi gracna --------

    def post(self, request, *args, **kwargs):
        form = CreateTicketForm(request.POST)
        existing_tickets = None

        if form.is_valid():
            bcrm_id = form.cleaned_data.get('bcrm_id')
            if Ticket.objects.filter(bcrm_id=bcrm_id).exists():
                existing_tickets = Ticket.objects.filter(bcrm_id=bcrm_id)
            else:
                ticket = form.save()
                ticket.save()
                return redirect('all_ticket')

        return render(request, 'ticket_create.html', {'form': form, 'existing_tickets': existing_tickets})

#-------------------------------- Ticket Update ---------------------------

class QualityUpdateForm(UpdateView):
    template_name = 'quality_ticket_edit.html'
    model = Ticket
    form_class = QualityCustomForm
    success_url = "/my_quality_ticket/"

class OPTicketUpdateForm(UpdateView):
    template_name = 'op_ticket_edit.html'
    model = Ticket
    form_class = OPCustomForm
    success_url = "/all_ticket/"


class TechTicketUpdateForm(UpdateView):
    template_name = 'tech_ticket_edit.html'
    model = Ticket
    form_class = TechCustomForm
    success_url = "/all_ticket/"

#    def get_success_url(self):
#        return reverse_lazy (self.request.META.get('HTTPS_REFERER'))


class CfTicketUpdateForm(UpdateView):
    template_name = 'conf_ticket_edit.html'
    model = Ticket
    form_class = ConfCustomForm
    success_url = "/all_ticket/"


#---------------------------------- Handler ---------------------------------

def custom_404(request, exception):
    return render(request, '404.html', status=404)

