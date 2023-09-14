$(function () {
    $.datepicker.setDefaults($.datepicker.regional['es-MX']); // Set Spanish locale for Mexico
    $("#inputBirthday").datepicker({
        dateFormat: 'dd/mm/yy', // Configura el formato de fecha a "dd/mm/yyyy"
        changeMonth: true,
        changeYear: true,
        yearRange: "1900:{{ 'now'|date:'Y' }}" // Ajusta el rango de años según tus necesidades
    });
});

$(document).ready(function(){
    var table = $('#datatablesSimple').DataTable({
       orderCellsTop: true,
       fixedHeader: true 
    });
    //Creamos una fila en el head de la tabla y lo clonamos para cada columna
    $('#datatablesSimple thead tr').clone(false).appendTo( '#datatablesSimple thead' );
    $('#datatablesSimple thead tr:eq(1) th').each( function (i) {
        var title = $(this).text(); //es el nombre de la columna
        $(this).html( '<input type="text" placeholder="Buscar Por '+title+'" />' );
        $( 'input', this ).on( 'keyup change', function () {
            if ( table.column(i).search() !== this.value ) {
                table
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        } );
    } );   
});