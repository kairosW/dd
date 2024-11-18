document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        let isValid = true;

        
        document.querySelectorAll('.error-message').forEach(function (msg) {
            msg.remove();  
        });

        
        document.getElementById('buscar-form').onsubmit = function(event) {
            event.preventDefault();
            const rutInput = document.getElementById('rut'); 
            const rut = rutInput.value.trim(); 
            const rutRegex = /^(?:[0-9]{1,3}(?:\.[0-9]{3})*|[0-9]{7,8})-([0-9kK])$/;
    
            
            if (!rutRegex.test(rut)) {
                showError('rut', 'El RUT no es válido. Debe seguir el formato: 12.673.458-9 o 12458673-9.');
                isValid = false;
            } else {
                console.log('RUT válido:', rut); 
                document.getElementById('rutDisplay').innerText = `RUT ingresado: ${rut}`;
            }
        };



       
        const nombre = document.getElementById('nombre') ? document.getElementById('nombre').value : '';
        if (nombre.trim() === '') {
            showError('nombre', 'El campo Nombre es obligatorio.');
            isValid = false;
        }

      
        const apellido = document.getElementById('apellido') ? document.getElementById('apellido').value : '';
        if (apellido.trim() === '') {
            showError('apellido', 'El campo Apellido es obligatorio.');
            isValid = false;
        }

       
        const comuna = document.getElementById('comuna') ? document.getElementById('comuna').value : '';
        if (comuna.trim() === '') {
            showError('comuna', 'El campo Comuna es obligatorio.');
            isValid = false;
        }

        
        const direccion = document.getElementById('direccion') ? document.getElementById('direccion').value : '';
        if (direccion.trim() === '') {
            showError('direccion', 'El campo Dirección es obligatorio.');
            isValid = false;
        }

        
        const telefono = document.getElementById('telefono') ? document.getElementById('telefono').value : '';
        const telefonoRegex = /^[0-9]{9,12}$/;
        if (telefono && !telefonoRegex.test(telefono)) {
            showError('telefono', 'El teléfono debe tener entre 9 y 12 dígitos.');
            isValid = false;
        }

      
        if (!isValid) {
            event.preventDefault();
        }
    });

    
    function showError(inputId, message) {
        const inputField = document.getElementById(inputId);
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.style.color = 'red';
        errorDiv.style.fontSize = '0.9em';
        errorDiv.textContent = message;

        
        inputField.parentNode.appendChild(errorDiv);
    }
});
