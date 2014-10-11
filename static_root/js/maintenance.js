$('#follow').on('shown.bs.modal', function() {
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
                      message: 'The subject is required'
                  },
                  stringLength: {
                        min: 6,
                        max:6,
                        message: 'The subject must be 6 characters'
                  },
                  integer: {
                        message: 'The value is not an integer'
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