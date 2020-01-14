//Varibles
const $sc = $("#select_carrera"); 

$(document).ready(function(){

    $sc.change(function(){ //Cada vez que la opcion del select "1" cambie
      console.log($sc.val())
      //$("#select_carrera option[value='0']").prop("selected", false);
      
  }); 
});
