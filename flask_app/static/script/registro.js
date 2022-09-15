var formulario = document.getElementById('formu');
formulario.onsubmit = function(e){
    e.preventDefault();
    var formData = new FormData(formu)
    fetch("/signin", {method: 'POST', body: formData})
    .then(response => response.json())
    .then(data => {
        console.log(data)
        if (data.message == 'correcto'){
            window.location.href = '/wall';
        }
        var alertMessage = document.getElementById('alerta');
        alertMessage.innerText = data.message;
        alertMessage.classList.add('alert');
        alertMessage.classList.add('alert-danger');
    })
}
