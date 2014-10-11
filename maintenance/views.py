from django.http import *
import json
from ielecom.form import *
from maintenance.models import *
from django.core.mail import send_mail


def follow_d(request):
    if request.method == 'POST':
        form = FollowF(request.POST)
        response = {}
        if form. is_valid():
            try:
                db = FollowM.objects.get(serial=request.POST['serial'])
                status = str(db.status)
                if status == 'Wait':
                    status_pm = ' is waiting for check'
                elif status == 'Check':
                    status_pm = ' is chacking call for price'
                else:
                    status_pm = ' successfully repaired'

                detail = str(db.device)
                detail_split = detail.split(' ==> ')
                device = detail_split[0]
                customer = detail_split[1]
                response.update({'pm': 'success', 'message': 'Hi dear '+customer+' your device  '+device+' '+status_pm})
                return HttpResponse(json.dumps(response), mimetype='application/javascript')
            except:
                response.update({'pm': 'error', 'message': 'not_save'})
                return HttpResponse(json.dumps(response), mimetype='application/javascript')


        else:
            response.update({'pm': 'error', 'message': 'validetor_error'})
            return HttpResponse(json.dumps(response), mimetype='application/javascript')

