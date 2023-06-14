from django.urls import path
from django.conf.urls import url, handler404
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from .views import * 


urlpatterns = [
    path('', user_login, name='user-login'),
    path('logout/', logout, name='logout'),
#---ticket view
    path('all_ticket/', AllTicketView.as_view(), name='all_ticket'),
    path('team_ticket/', TeamTicketView.as_view(), name='team_ticket'),
    path('my_quality_ticket/', QualityTicketView.as_view(), name='my_quality_ticket'),
#---dontneet pages
    path('op_ticket/', OperationalTicketView.as_view(), name='op_ticket'),
    path('tech_ticket/', TechnicalTicketView.as_view(), name='tech_ticket'),
    path('conf_ticket/', ConfTicketView.as_view(), name='conf_ticket'),
#---ticket update
    path('<pk>/op_update', OPTicketUpdateForm.as_view(), name='op_update'),
    path('<pk>/tech_update', TechTicketUpdateForm.as_view(), name='tech_update'),
    path('<pk>/conf_update', CfTicketUpdateForm.as_view(), name='conf_update'),
#---ticket detail
    path('<pk>/ticket_detail/', TicketDetailView.as_view(), name='ticket_detail'),
#---ticket create
    path('create_ticket/', TicketCreateView.as_view(), name='create_ticket'),
#---quality pages
    path('<pk>/quality_ticket_detail/', QualityUpdateForm.as_view(), name='quality_ticket_detail'),
#---pass reset
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('user-login')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

handler404 = 'fond_main.views.custom_404'
