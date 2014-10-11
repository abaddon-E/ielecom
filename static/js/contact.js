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
            subject: {
              validators: {
                  notEmpty: {
                      message: 'پر کردن این فیلد الزامی است'
                  },
                  stringLength: {
                        min: 5,
                        message: 'موضوع بیش  از ۵ حرف میباشد'
                    }

              }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: 'پر کردن این فیلد الزامی است'
                    },
                    emailAddress: {
                        message: 'ایمیل وارد شده صحیح نمی باشد'
                    }
                }
            },
            message: {
                validators: {
                    notEmpty: {
                        message: 'پر کردن این فیلد الزامی است'
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