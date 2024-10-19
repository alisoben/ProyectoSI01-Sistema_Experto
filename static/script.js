document.addEventListener("DOMContentLoaded", function() {
    // Manejar la selección de preferencias alimenticias
    document.querySelectorAll("button[data-group='preferencias']").forEach(function(button) {
        button.addEventListener("click", function() {
            const index = button.getAttribute("data-index");
            let preferencias = document.getElementById("preferencias").value.split('');

            // Alternar entre 0 y 1 al hacer clic
            if (preferencias[index] === '0') {
                preferencias[index] = '1';
                button.classList.add("selected");
            } else {
                preferencias[index] = '0';
                button.classList.remove("selected");
            }

            // Actualizar el valor del campo oculto
            document.getElementById("preferencias").value = preferencias.join('');
        });
    });

    // Manejar la selección de condiciones médicas
    document.querySelectorAll("button[data-group='condiciones']").forEach(function(button) {
        button.addEventListener("click", function() {
            const index = button.getAttribute("data-index");
            let condiciones = document.getElementById("condiciones").value.split('');

            // Alternar entre 0 y 1 al hacer clic
            if (condiciones[index] === '0') {
                condiciones[index] = '1';
                button.classList.add("selected");
            } else {
                condiciones[index] = '0';
                button.classList.remove("selected");
            }

            // Actualizar el valor del campo oculto
            document.getElementById("condiciones").value = condiciones.join('');
        });
    });
});

// Script para actualizar los valores de los sliders
function updateSliderValue(sliderId, labelId) {
    var slider = document.getElementById(sliderId);
    var label = document.getElementById(labelId);
    label.innerHTML = slider.value;
}
