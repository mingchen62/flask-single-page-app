$(document).ready(function() {
  console.log("ready!");

  $('#try-again').hide();

  // on form submission ...
  $('form').on('submit', function() {

    console.log("the form has beeen submitted");

    // grab values
    //valueOne = $('input[name="location"]').val();
    //console.log(valueOne)
    valueTwo = $("#message").val();
    alert($("#message").val())
    console.log(valueTwo)

    $.ajax({
      type: "POST",
      url: "/",
      dataType: 'json',
      contentType: 'application/json',
      data : JSON.stringify( {'story': valueTwo }),
      success: function(results) {
        if (results.summary.length > 0) {
          //$('input').hide();
          $('#try-again').show();
          //console.log(results.items[randNum]);
          $('#results').html(results.summary)
          // $('input').val('')
        } else {
          $('#results').html('Something went terribly wrong! Please try again.')
        }
      },
      error: function(error) {
        console.log(error)
      }
    });

  });

  $('#try-again').on('click', function(){
    $('input').val('').show();
    $('#try-again').hide();
    $('#results').html('');
  });

});
