function apply_form_field_error(fieldname, error) {
  // console.log("this is the field name", fieldname);
    var fieldNameId = $("#id_" + fieldname);
    var errorMessage = error[0].message;
    // console.log(fieldNameId, errorMessage);
    // fieldNameId.css({"border": "solid red 1px"})
    container = $("#id_" + fieldname),
    error_msg = $("<span />").addClass("help-inline ajax-error").text(errorMessage).css({color: 'white'});
    container.addClass("error").css({border: 'solid #ad181a 2px'});
    error_msg.insertAfter(fieldNameId);
}

function clear_form_field_errors(form) {
  // console.log("the clear form ran");
    $(".ajax-error", $(form)).remove();
    $(".error", $(form)).removeClass("error").css({border: 'solid black 2px'});
}



var add_newsletter = function (form) {
    $.ajax({
        url : form.attr('action'), // the endpoint
        type : form.attr('method'), // http method
        data : form.serialize(), // data sent with the post request
        // handle a successful response

        beforeSend:function() { 
        clear_form_field_errors(form);
      },
        success : function(data) {
          $(form).fadeOut(300, function(){ 
            $(this).html('<span class="text-center newsletter-text" >Thank You! We will keep you informed.</span>').fadeIn();
          });
        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
          var errors = $.parseJSON(xhr.responseText);
          var slime = $.parseJSON(errors.form_errors)
          $.each(slime, function(index, value){
            apply_form_field_error(index, value);
          })
        }

    });
};



$(document).ready(function(){
  $('#newsletter-form').on('submit', function(e){
    e.preventDefault()
    var $form = $(this); 
        add_newsletter($form);
    });
});