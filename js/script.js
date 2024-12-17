document.addEventListener('DOMContentLoaded', function(){
    const anuncio = document.getElementById('anuncio');
    const botoncerrar = document.getElementById('cerrar');


    if(anuncio && botoncerrar){
        botoncerrar.addEventListener('click', function(){
            anuncio.style.display = 'none';
        })
    }else{
        console.error("El anuncio el boton de cierre no se encontraron");
    }
});

