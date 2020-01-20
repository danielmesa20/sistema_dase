
var options = {
    tipo_beneficio : ["desempeño","honor","Excelencia academica"],
    carrera : ["ingenieria","Psicologia","Diseño"],
    materias : ["1","2","3","4","5"],
    indice : ["10","11","12"],
    departamento:  ["Ingenieria","Matematicas","Humanidades"],
    trimestre: ["1","2","3"],
  }

function change_option() {

    var selected = $("#primary").val();
   
    $("#secondary").prop("disabled", false);
    $('#secondary').empty();

    options[selected].forEach(function(element,index){
        $('#secondary').append('<option value="'+element+'">'+element+'</option>');
    });

    $('#secondary').selectpicker('refresh');
}