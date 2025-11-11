$(document).ready(function (){
    $("#agregarDireccion").submit(function (e) {
        var Calle = $("#Calle").val();
        var Numero = $("#Numero").val();
        var Descripcion =$("#Descripcion").val();
        var Cod_post =$("#Cod_post").val();

        var msg = "";
        let enviar = false

        /*if Calle */
        if (Calle.trim().length < 1 || Calle.trim().length > 30) {
            msg += "<p class='text-muted'>" + "La Calle no puede quedar en blanco y tienes como maximo 30 carateres" + "</p>";
            enviar = true;
        }

        /*if Numero Direccion */
        if (Numero.trim().length < 1 || Numero.trim().length > 5) {
            msg += "<p class='text-muted'>" + "El Numero de casa no puede quedar en blanco y su maximo es de 5 numeros" + "</p>";
            enviar = true;
        }

        /* if descripcion*/
        if (Descripcion.trim().length < 4 || Descripcion.trim().length > 300) {
            msg += "<p class='text-muted'>" + "La descripción debe contener entre 4 y 300 caracteres." + "</p>";
            enviar = true;
        }

        /* if codigo postal*/
        if (Cod_post.trim().length < 1 || Cod_post.trim().length > 8) {
            msg += "<p class='text-muted'>" + "El Codigo postal no puede quedar en blanco y tienes como maximo 8 carateres" + "</p>";
            enviar = true;
        }

        /* Evaluacion de bandera para enviar el formulario */
        if (enviar) {
            e.preventDefault();
            $("#warning").html(msg);
        }
        else {
            $("#warning").html("Direccion agregada");
        }
        
    });
});
