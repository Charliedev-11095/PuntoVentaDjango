$(function () {
    $.datepicker.setDefaults($.datepicker.regional['es-MX']); // Set Spanish locale for Mexico
    $("#inputBirthday").datepicker({
        dateFormat: 'dd/mm/yy', // Configura el formato de fecha a "dd/mm/yyyy"
        changeMonth: true,
        changeYear: true,
        yearRange: "1900:{{ 'now'|date:'Y' }}" // Ajusta el rango de años según tus necesidades
    });
});

// ------------------------------------------------------------------------------------------------------------

$(document).ready(function() {
    var table = $('#datatablesSimple').DataTable({
        orderCellsTop: true,
        fixedHeader: true
    });

    // Creamos una fila en el head de la tabla y lo clonamos para cada columna
    $('#datatablesSimple thead tr').clone(false).appendTo('#datatablesSimple thead');
    
    $('#datatablesSimple thead tr:eq(1) th').each(function(i) {
        var title = $(this).text(); // es el nombre de la columna
        $(this).html('<input type="text" placeholder="Buscar Por ' + title + '" />');
        

        $('input', this).on('keyup change', function() {
            if (table.column(i).search() !== this.value) {
                table
                    .column(i)
                    .search(this.value)
                    .draw();
                
                // Realiza una solicitud AJAX para obtener los datos filtrados
                obtenerDatosFiltrados(this.value);
            }
        });
    });

    // Función para realizar la solicitud AJAX
    function obtenerDatosFiltrados(filtro) {
        $.ajax({
            url: '/lista_usuarios/', // Reemplaza esto con la URL correcta a tu vista
            method: 'GET',
            data: {filtro: filtro}, // Envia el valor del filtro al servidor
            dataType: 'json',
            success: function(data) {
                // Manipula los datos recibidos aquí y actualiza la tabla o el array de datos
                console.log(data); // Muestra los datos en la consola para depuración
            },
            error: function(error) {
                console.error('Error al obtener datos:', error);
            }
        });
    }
});

