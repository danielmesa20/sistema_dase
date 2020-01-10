const $f1 = $("#filtro1");
const $f2 = $("#filtro2");
const $d = $("#dato");

var c = ['Psicologia', 'Ingenieria', 'Economia']
var b = ['Excelencia','Honor','Desempeño']

$(document).ready(function(){

    $f1.change(function(){

    // Segundo select 
    if($f1.val() == "Carrera" || $f1.val() == "Beneficio" || $f1.val() == "Trimestre"){     // si una region es seleccionada quitara la propiedad disabled
     
      $f2.prop('disabled', false);

      //LLenar el segundo select

      if($f1.val() == "Carrera"){
        for(var i=0; i<c.length; i++)
          filtro2.options[i]= new Option(c[i],c[i]);
      }else if ($f1.val() == "Beneficio"){
        for(var i=0; i<b.length; i++)
          filtro2.options[i]= new Option(b[i],b[i]);
      }
      
    }else{
      $f2.prop('disabled', true);                                                           // si una comuna no esta seleccionada mantendra la propiedad disabled
    }

    // Text field
    if($f1.val() == "Nombre" || $f1.val() == "Cedula"){        //si una region es seleccionada quitara la propiedad disabled
      $d.prop('disabled', false);
    }else{
      $d.prop('disabled', true);           //si una comuna no esta seleccionada mantendra la propiedad disabled
      dato.value="";
    }

  });
});