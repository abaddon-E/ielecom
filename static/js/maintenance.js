$('#CheckSerial').on('shown.bs.modal', function() {
    $('#FollowForm').bootstrapValidator('resetForm', true);
});
$(document).ready(function() {
    $('#FollowForm').bootstrapValidator({
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        live: 'enabled',
        fields: {
            serial: {
              validators: {
                  notEmpty: {
                      message: 'پر کردن این فیلد الزامی است'
                  },
                  stringLength: {
                        min: 6,
                        max:6,
                        message: 'کد پیگیری شش رقم می باشد'
                  },
                  digits: {
                        message: 'کد پیگیری صحیح نمی باشد'
                  }

              }
            }


        }


    })
    .on('error.field.bv',function(e, data) {
             $('#CheckSerial').attr('disabled','disabled')
    })
    .on('success.field.bv',function(e, data) {
             $('#CheckSerial').removeAttr('disabled','disabled')
    })


});