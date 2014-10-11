from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
import json
from ielecom.form import *
from contact.models import *
import datetime
from sendfile import sendfile


def on_load(request):
    form = Subscribe()
    return render_to_response('onload.html', {'form': form}, context_instance=RequestContext(request))


def home(request):
    form_sub = FollowF()
    return render_to_response('home.html', {'form_sub': form_sub, 'title': 'home'},
                              context_instance=RequestContext(request))


def about(request):
    return render_to_response('about.html', {'title': 'about'}, context_instance=RequestContext(request))


def contact_tp(request):
    form_sub = FollowF()
    form_contact = ContactForm()
    var = {'title': 'contact', 'form_sub': form_sub, 'form_contact': form_contact}
    return render_to_response('contact.html', var, context_instance=RequestContext(request))


def subscribe(request):
    if request.method == 'POST':
        response_dict = {}
        form = Subscribe(request.POST)
        if form. is_valid():
            email = request.POST['email']
            client_ip = request.META['REMOTE_ADDR']
            date = datetime.datetime.today()
            db_save = Email(email=email, ip=client_ip, date=date)
            db_save.save()
            response_dict.update({'pm': 'success'})
            return HttpResponse(json.dumps(response_dict), mimetype='application/javascript')

        else:
            send = "server validation error"
            response_dict.update({'server_response': send, 'pm': 'error'})
            return HttpResponse(json.dumps(response_dict), mimetype='application/javascript')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        response_dict = {}
        if form. is_valid():
            date = datetime.datetime.today()
            db_save = Contact(
                subject=request.POST['subject'], email=request.POST['email'],
                message=request.POST['message'], date=date,
                ip=request.META['REMOTE_ADDR']
            )
            db_save.save()
            response_dict.update({'pm': 'success', 'message': 'your post success'})
            return HttpResponse(json.dumps(response_dict), mimetype='application/javascript')
        else:
            send = "server validator error"
            response_dict.update({'message': send, 'pm': 'error'})
            return HttpResponse(json.dumps(response_dict), mimetype='application/javascript')


def download(request):
    try:
        return sendfile(
            request, '/var/sites/ielecom/media/'+request.GET['dl'],
            attachment=True,
            attachment_filename=request.GET['dl']
        )
    except:
        return render_to_response('404.html', context_instance=RequestContext(request))

