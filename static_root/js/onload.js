$('#contact').on('shown.bs.modal', function() {
    $('#ContactForm').bootstrapValidator('resetForm', true);
});
$(document).ready(function() {
    $('#ContactForm').bootstrapValidator({
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        live: 'enabled',
        fields: {

            email: {
                validators: {
                    notEmpty: {
                        message: 'پر کردن این فیلد اجباری است'
                    },
                    emailAddress: {
                        message: 'فرمت ایمیل وارد شده صحیح نیست'
                    }
                }
            }

        }


    })
    .on('error.field.bv',function(e, data) {
             $('#SendContact').attr('disabled','disabled')
    })
    .on('success.field.bv',function(e, data) {
             $('#SendContact').removeAttr('disabled','disabled')
    })


});