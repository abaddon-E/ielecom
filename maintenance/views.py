from django.http import *
import json
from ielecom.form import *
from maintenance.models import *
from django.utils.translation import ugettext as _


def follow_d(request):
    if request.method == 'POST':
        form = FollowF(request.POST)
        response = {}
        if form. is_valid():
            try:
                db = FollowM.objects.get(serial=request.POST['serial'])
            except:
                response.update({'pm': 'error', 'message': _('not_save')})
                return HttpResponse(json.dumps(response))
            # -*- coding: utf-8 -*-
            status = db.status
            if status == 'Wait':
                status_pm = _(' is waiting for check')
            elif status == 'Check':
                status_pm = _(' is chacking call for price')
            else:
                status_pm = _(' successfully repaired')
            response.update({'pm': 'success', 'message': _(' your device  ')+status_pm})
            return HttpResponse(json.dumps(response))

        else:
            response.update({'pm': 'error', 'message': _('validetor_error')})
            return HttpResponse(json.dumps(response))
