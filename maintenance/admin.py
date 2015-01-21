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
    if len(selected) > 4:
        message_bit = _('You cant select more than four field for this action')
        self.message_user(request, message_bit, level='error')
    else:
        db = FollowM.objects.get(serial=selected[0])
        date = gregorian_to_jd(str(db.date))
        response = {'date': date}
        j = 0
        for select in selected:

            db = FollowM.objects.get(serial=select)
            device_owner = str(db.device)
            split = device_owner.split(' ==> ')
            device = split[0]
            owner = split[1]
            detail = db.detail
            try:
                owner_db = Customer.objects.get(fullname=owner)
                if len(str(owner_db.phone)) > 1:
                    phone = str(owner_db.phone)
                else:
                    phone = str(owner_db.mobile)
            except:
                phone = ''

            i = str(j)
            response.update({
                'num_'+i: j + 1,
                'follow_'+i: select,
                'model_'+i: device,
                'name_'+i: owner,
                'phone_'+i: phone,
                'detail_'+i: detail
            })
            j = j + 1

        return render_to_response('resid.html', response)

print_follow.short_description = _('print that follow')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('serial', 'device')
    search_fields = ('serial',)
    list_filter = ('date',)
    date_hierarchy = 'date'
    actions = [print_follow]

admin.site.register(FollowM, FollowAdmin)
