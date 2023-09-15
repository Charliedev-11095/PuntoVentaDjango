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

let dataTable;
let dataTableIsInitialized = false;

const DataTableOptions = {
    columDefs: [
        {className: 'centered', targets: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ]},
        {orderable: false, targets: [9, 10, 11]},
        {searchable: false, targets: [1,2,3,4,5,6,7,8,9,10]},
    ],
    pageLength: 4,
    destroy: true,
};

const initDataTable = async () => {
    if(dataTableIsInitialized){
        dataTable.destroy();
    }
    await listUsuarios();

    // Combina el código de DataTables con la creación de columnas de búsqueda
    $('#tableUsuarios thead tr').clone(true).appendTo( '#tableUsuarios thead' );

    $('#tableUsuarios thead tr:eq(1) th').each( function (i) {
        var title = $(this).text(); //es el nombre de la columna
        $(this).html( '<input type="text" placeholder="Search...'+title+'" />' );

        $( 'input', this ).on( 'keyup change', function () {
            if ( dataTable.column(i).search() !== this.value ) {
                dataTable
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        });
    });

    // Inicializa el DataTable después de configurar las columnas de búsqueda
    dataTable = $('#tableUsuarios').DataTable(DataTableOptions);
    dataTableIsInitialized = true;
};

const listUsuarios = async () => {
    try{
        const response = await fetch('/lista_usuarios/');
        const datos = await response.json();
        console.log(datos);
        let content = '';
         datos.usuarios.forEach((usuario,index) => {
            
            let rolTexto = '';
            if (usuario.is_staff) {
                rolTexto = 'Administrador';
            } else if (usuario.es_vendedor) {
                rolTexto = 'Vendedor';
            } else {
                rolTexto = 'Otro Rol';
            }
            
            let estadoTexto = usuario.is_active
            ? '<div class="badge bg-success text-white rounded-pill">Activo</div>'
            : '<div class="badge bg-danger text-white rounded-pill">Inactivo</div>';
            content += `
            <tr>
                <td class="centered">${index+1}</td>
                <td class="centered">${usuario.user_name}</td>
                <td class="centered">${usuario.nombre}</td>
                <td class="centered">${usuario.apellido_paterno}</td>
                <td class="centered">${usuario.apellido_materno}</td>
                <td class="centered">${usuario.gender}</td>
                <td class="centered">${usuario.birth_date}</td>
                <td class="centered">${usuario.email}</td>
                <td class="centered">${usuario.phone}</td>
                <td class="centered">${rolTexto}</td>
                <td class="centered">${estadoTexto}</td>
                <td class="centered"><a href="/configperfil/"><i class="fas fa-edit"></i> editar</a> | <a href="/seguridad/"><i class="fas fa-trash-alt"></i> eliminar</a></td>
            </tr>
            `;
        });
        tableBody_usuarios.innerHTML = content;  
    }catch(ex){
    }
};

window.addEventListener('load', async() => {
    await initDataTable();
});
