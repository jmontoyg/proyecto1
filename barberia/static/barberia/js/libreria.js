console.log("Hola mundo")

function eliminarRegistro(ruta){
    if(confirm('Está seguro?')){
        location.href = ruta;
    }
}

function cargarUsuarios(ruta){
    alert("hola")
    $.ajax({
        method: "GET",
        url: ruta,
        //data: { name: "John", location: "Boston" },
        cache: false
    })
    .done(function( respuesta ) {
        $( "#respuesta_ajax" ).html( respuesta );
    });
}