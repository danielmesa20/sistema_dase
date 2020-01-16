
var options = {
  beneficio : ["Excelencia","Honor","Desempeño"],
  carrera : ["Sistemas","Psicologia","Economia"],
  materias : ["1","2","3","4","5"],
  indice : ["10","11","12"],
  departamento:  ["Ingenieria","Matematicas","Humanidades"],
  trimestre: ["1","2","3"],
}

const $sc = $("#primary"); 

var beneficio = ["Spain","Germany","France"];
var carrera = ["red","green","blue"];

$(document).ready(function(){

      $('#primary').on('changed.bs.select', function (e, clickedIndex, isSelected, previousValue) {

        var selected = $('#primary').val();

        $('#secondary').empty();

        options[selected].forEach(function(element,index){
          $('#secondary').append('<option value="'+element+'">'+element+'</option>');
        });

        $('#secondary').selectpicker('refresh')
      
    }); 
});