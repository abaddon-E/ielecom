$('#SendContact').on('shown.bs.modal', function() {
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
                      message: 'The subject is required'
                  },
                  stringLength: {
                        min: 5,
                        message: 'The subject must more than 5 characters'
                    }

              }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: 'The email address is required'
                    },
                    emailAddress: {
                        message: 'The email address is not valid'
                    }
                }
            },
            message: {
                validators: {
                    notEmpty: {
                        message: 'The comment is required'
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