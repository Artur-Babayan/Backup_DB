from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .models import *

def user_login_required(function):
    def wrapper(request, *args, **kw):
        if request.user.groups.filter(name='All Levels').exists():
            return redirect('all_ticket')
        elif request.user.groups.filter(name='Operational Level').exists():
            return redirect('op_ticket')
        elif request.user.groups.filter(name='Technical Level').exists():
            return redirect('tech_ticket')
        elif request.user.groups.filter(name='Config Level').exists():
            return redirect('conf_ticket')
        else:
            return function(request, *args, **kw)
    return wrapper

