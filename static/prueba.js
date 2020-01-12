//Varibles
const $s1 = $("#select1");  //Select principal
const $s2 = $("#select2");  //Select carreras
const $s3 = $("#select3");  //Select tipos de beneficio
const $d = $("#data");      // input text

/*
$(document).ready(function(){

    $s1.change(function(){ //Cada vez que la opcion del select "1" cambie

    if($s1.val() == "Carrera" || $s1.val() == "Beneficio" || $s1.val() == "Trimestre"){

      // El input text deja de ser requerido
      $d.prop('required',false);

    }else{
      $d.prop('required',true);
      $s2.prop("disabled", "true");
      $s3.prop("disabled", "true");
    }

  });
});
*/