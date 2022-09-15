var formLogin = document.getElementById('formlogin'); //Obteniendo el formulario

/* Vamos a escuchar cuando se realice el evento ON SUBMIT */
formLogin.addEventListener("submit", function (event) {
    event.preventDefault(); /* Previene el comportamiento por default de mi formulario */

    //Creamos una variable con todos los datos del formulario
    var formulario = new FormData(formLogin);
    /*
    formulario = {
        "email": "elena@codingdojo.com",
        "password": "1234"
    } 
     */
    fetch("/login-2", {method: 'POST', body: formulario})
        .then(response => response.json())
        .then(data => {
            console.log(data);

            if(data.message == "correcto") {
                window.location.href = "/wall";
            }

            if(data.message == "Wrong email"  || data.message == "Incorrect password"){
                var mensajeAlerta = document.getElementById('alerta'); //El elemento con identificador mensajeAlerta
                mensajeAlerta.innerText = data.message;
                mensajeAlerta.classList.add('alert');
                mensajeAlerta.classList.add('alert-danger');
            }
            
            
        });
        /*
        function x(data){
            console.log(data);
        }
         */
})


async function api(){
    var response = await fetch('https://api.nasa.gov/planetary/apod?api_key=eDTY9trq8OXvDQtUuP5Y1SePEvBANk74xXHiiWk5');
    var responseJson = await response.json();
    var text = responseJson.title;
    var contenedor_1= document.querySelector('#titulo');
    contenedor_1.innerHTML = "<p> '"+text+ "'</p>"
    var date = responseJson.date;
    var contenedor_2= document.querySelector('#fecha');
    contenedor_2.innerHTML = "<p> '"+date+ "'</p>"
    var desc = responseJson.explanation;
    var contenedor_3= document.querySelector('#descripcion');
    contenedor_3.innerHTML = "<p> '"+desc+ "'</p>"
    contenedor_3.classList.add('dec');
    var img = responseJson.url;
    var contenedor = document.querySelector('#c_multimedia');
    contenedor.innerHTML = "<img src='" +img+ "' alt = 'image'/>"
    contenedor.classList.add('nasa');
}

function cambiImg(element){
    element.src = "https://images-assets.nasa.gov/image/PIA02442/PIA02442~small.jpg"
}

function cambiImg2(element){
    element.src = "https://images-assets.nasa.gov/image/PIA00342/PIA00342~medium.jpg"
}


function cambiImg_2(element){
    element.src = "https://images-assets.nasa.gov/image/PIA16853/PIA16853~small.jpg"
}

function cambiImg2_2(element){
    element.src = "https://images-assets.nasa.gov/image/PIA11800/PIA11800~medium.jpg"
}


