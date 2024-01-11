$(document).ready(function() {
	var oTable = $('table#dataTables, table.dataTables').dataTable( {
		"language": {
            "url": path_base + "json/Spanish.json"
        },
		"iDisplayLength": 25
	})
	.removeClass( 'display' )
	.addClass('table table-striped table-bordered');
} );