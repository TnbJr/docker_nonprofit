function apply_form_field_error(fieldname, error) {
    var fieldNameId = $("#id_" + fieldname);
    var errorMessage = error[0].message;
    if( fieldname === "captcha"){
      fieldNameId = $("#id_" + fieldname + "_1")
    }
    container = $("#id_" + fieldname)
    error_msg = $("<span />").addClass("help-inline ajax-error").text(errorMessage).css({color: '#191905'});
    fieldNameId.addClass("error").css({border: 'solid #ad181a 2px'});
    error_msg.insertAfter(fieldNameId);
}

function clear_form_field_errors(form) {
    $(".ajax-error", $(form)).remove();
    $(".error", $(form)).removeClass("error");
}


// function(){

// }

var send_form = function (form) {
    $.ajax({
        url : form.attr('action'), // the endpoint
        type : form.attr('method'), // http method
        data : form.serialize(), // data sent with the post request

        beforeSend:function() { 
        clear_form_field_errors(form);
      },
        success : function(data) {
          $(form).fadeOut(300, function(){ 
            $(this).html('<h3 class="text-center coming-soon"">Thank You For Contacting Us! <br> We will get back to you soon.</h3>').fadeIn();
          });
        },

        error : function(xhr,errmsg,err) {
          var errors = $.parseJSON(xhr.responseText);
          var form_errors = $.parseJSON(errors.form_errors)
          console.log(form_errors)
          $.each(form_errors, function(index, value){
            apply_form_field_error(index, value);
          })
          var $form = $('#contact-form')
          var key = errors.key
          var img_url = errors.img_url
          $form.find('img.captcha').attr('src', img_url)
          $form.find('input[name="captcha_0"]').val(key)
        }

    });
};


$(document).ready(function(){
  $('#contact-form').on('submit', function(e){
    e.preventDefault()
    var $form = $(this); 
        send_form($form);
    });

$(function() {
    // Add refresh button after field (this can be done in the template as well)
    $('img.captcha').after(
            $('<a href="#void" class="captcha-refresh">Refresh</a>')
            );

    // Click-handler for the refresh-link
    $('.captcha-refresh').click(function(){
        var $form = $(this).parents('form');
        var url = location.protocol + "//" + window.location.hostname + ":"
                  + location.port + "/captcha/refresh/";

        // Make the AJAX-call
        $.getJSON(url, {}, function(json) {
            $form.find('input[name="captcha_0"]').val(json.key);
            $form.find('img.captcha').attr('src', json.image_url);
        });

        return false;
    });
});
});