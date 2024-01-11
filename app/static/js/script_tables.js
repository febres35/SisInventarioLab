$(document).ready(function() {
    $('#example').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
        pageLength: 25,
        language: {
            paginate: {
                next: "Siguiente",
                previous: "Anterior"
            },
            info: "Mostrar _START_ a _END_  registros de _TOTAL_ articulos"
        }
    } );
} );