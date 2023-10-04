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

let dataTableUsuarios;
let dataTableUsuariosIsInitialized = false;
let dataTableMarcas;
let dataTableMarcasIsInitialized = false;

const DataTableOptionsUsuarios = {
    columDefs: [
        // Configuración de columnas para la tabla de usuarios
        { className: 'centered', targets: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] },
        { orderable: false, targets: [9, 10, 11] },
        { searchable: false, targets: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] },
    ],
    pageLength: 4,
    destroy: true,
};

const DataTableOptionsMarcas = {
    columDefs: [
        // Configuración de columnas para la tabla de marcas
        { className: 'centered', targets: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] },
        { orderable: false, targets: [9, 10, 11, 12] },
        { searchable: false, targets: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] },
    ],
    pageLength: 4,
    destroy: true,
};

const initDataTableUsuarios = async () => {
    if (dataTableUsuariosIsInitialized) {
        dataTableUsuarios.destroy();
    }
    await listUsuarios();

    $('#tableUsuarios thead tr').clone(true).appendTo('#tableUsuarios thead');

    $('#tableUsuarios thead tr:eq(1) th').each(function (i) {
        var title = $(this).text();
        $(this).html('<input type="text" placeholder="Buscar...' + title + '" />');

        $('input', this).on('keyup change', function () {
            if (dataTableUsuarios.column(i).search() !== this.value) {
                dataTableUsuarios
                    .column(i)
                    .search(this.value)
                    .draw();
            }
        });
    });

    dataTableUsuarios = $('#tableUsuarios').DataTable(DataTableOptionsUsuarios);
    dataTableUsuariosIsInitialized = true;
};

const initDataTableMarcas = async () => {
    if (dataTableMarcasIsInitialized) {
        dataTableMarcas.destroy();
    }
    await listMarcas();

    $('#tableMarcas thead tr').clone(true).appendTo('#tableMarcas thead');

    $('#tableMarcas thead tr:eq(1) th').each(function (i) {
        var title = $(this).text();
        $(this).html('<input type="text" placeholder="Buscar...' + title + '" />');

        $('input', this).on('keyup change', function () {
            if (dataTableMarcas.column(i).search() !== this.value) {
                dataTableMarcas
                    .column(i)
                    .search(this.value)
                    .draw();
            }
        });
    });

    dataTableMarcas = $('#tableMarcas').DataTable(DataTableOptionsMarcas);
    dataTableMarcasIsInitialized = true;
};

const listUsuarios = async () => {
    try {
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
                <td class="centered">
                <a href="/configperfil/editar/${usuario.id}/"><i class="fas fa-edit"></i> editar</a> 
                | 
                <a href="/seguridad/?id=${usuario.id}"><i class=" fas fa-trash-alt"></i> eliminar</a>
                </td>
            </tr>
            `;
        });
        tableBody_usuarios.innerHTML = content;  
    }catch(ex){
    }
};

const listMarcas = async () => {
    try {
        const response = await fetch('/lista_marcas/');
        const datos = await response.json();
        console.log(datos);
        let content = '';
         datos.marcas.forEach((marca,index) => {
            content += `
            <tr>
                <td class="centered">${index+1}</td>
                <td class="centered">${marca.nombre_de_la_marca}</td>
                <td class="centered">${marca.descripcion_marca}</td>
                <td class="centered"> <a href="/agregar_marca/"><i class="fas fa-plus"></i> agregar</a>
                 | 
                 <a href="/editar_marca/${marca.id}/"><i class="fas fa-edit"></i> editar</a>  
                 |
                 <a href="/eliminar_marca/"><i class=" fas fa-trash-alt"></i> eliminar</a></td>

            </tr>
            `;
        });
        tableBody_marcas.innerHTML = content;
    } catch (ex) {
    }
};

window.addEventListener('load', async () => {
    await initDataTableUsuarios();
    await initDataTableMarcas();
});
