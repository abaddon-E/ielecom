from django.contrib import admin
from maintenance.models import *
from django.utils.translation import ugettext as _
from django.http import *
from calender import Calverter
from django.shortcuts import render_to_response
admin.site.register(Customer)
admin.site.register(Device)

def gregorian_to_jd(date):
        fix_d = date.split('-')
        cal = Calverter()
        jd = cal.gregorian_to_jd( int(fix_d[0]), int(fix_d[1]), int(fix_d[2]))
        wday = cal.jwday(jd)
        final_d = cal.jd_to_jalali(jd)
        jalali = str(final_d[0])+'/'+ str(final_d[1])+'/'+ str(final_d[2])
        return jalali


def print_follow(self, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    if len(selected) > 3:
        message_bit = _('You cant select more than three field for this action')
        self.message_user(request, message_bit, level='error')
    else:
        db = FollowM.objects.get(serial=selected[0])
        date = gregorian_to_jd(str(db.date))
        response = {'date':date}

        device_owner = str(db.device)
        split = device_owner.split(' ==> ')
        device = split[0]
        owner = split[1]
        response.update({'num':1,
                        'follow': selected[0],
                        'model': device,
                        'name':owner
                        })
        if len(selected) > 1:
            db_b = FollowM.objects.get(serial=selected[1])
            device_owner_b = str(db_b.device)
            split_b = device_owner_b.split(' ==> ')
            device_b = split_b[0]
            owner_b = split_b[1]
            response.update({
                'num_2':2,
                'follow_2': selected[1],
                'model_2':device_b,
                'name_2':owner_b
                })
            if len(selected) == 3:
                db_c =FollowM.objects.get(serial=selected[2])
                device_owner_c = str(db_c.device)
                split_c = device_owner_c.split(' ==> ')
                device_c = split_c[0]
                owner_c = split_c[1]
                response.update({
                    'num_3':3,
                    'follow_3': selected[2],
                    'model_3':device_c,
                    'name_3':owner_c
                    })


        return render_to_response('resid.html',response)

print_follow.short_description = _('print that follow')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('serial', 'device')
    search_fields = ('serial',)
    list_filter = ('date',)
    date_hierarchy = 'date'
    actions = [print_follow]

admin.site.register(FollowM, FollowAdmin)
