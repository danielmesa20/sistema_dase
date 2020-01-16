
var options = {
  color : ["red","green","blue"],
  country : ["Spain","Germany","France"]
}

$(document).ready(function(){

  console.log("entre");

    var fillSecondary = function(){

      var selected = $('#primary').val();

      $('#secondary').empty();

      options[selected].forEach(function(element, index){
        $('#secondary').append('<option value="'+element+'">'+element+'</option>');
      });
      
    }

    $('#primary').change(fillSecondary);
    fillSecondary();
    
});