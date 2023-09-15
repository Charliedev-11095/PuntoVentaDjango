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
  
    dataTable = $('#tableUsuarios').DataTable({});
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
                <td>${index+1}</td>
                <td>${usuario.user_name}</td>
                <td>${usuario.nombre}</td>
                <td>${usuario.apellido_paterno}</td>
                <td>${usuario.apellido_materno}</td>
                <td>${usuario.gender}</td>
                <td>${usuario.birth_date}</td>
                <td>${usuario.email}</td>
                <td>${usuario.phone}</td>
                <td>${rolTexto}</td>
                <td>${estadoTexto}</td>
                <td><a href="/configperfil/"><i class="fas fa-edit"></i></a> | <a href="/seguridad/"><i class="fas fa-trash-alt"></i></a></td>

                
            `;
            
        });
        tableBody_usuarios.innerHTML = content;  
    }catch(ex){
    }
};
window.addEventListener('load', async() => {
await initDataTable();
});