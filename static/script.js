document.addEventListener("DOMContentLoaded", function() {
    const restricciones = [];
    const condiciones = [];

    document.querySelectorAll("button[data-group='preferencias']").forEach(function(button) {
        button.addEventListener("click", function() {
            const valor = button.getAttribute("data-value");
            const index = restricciones.indexOf(valor);
            
            if (index === -1) {
                restricciones.push(valor);
                button.classList.add("selected");
            } else if (index !== -1) {
                restricciones.splice(index, 1);
                button.classList.remove("selected");
            }

            document.getElementById("preferencias").value = restricciones.join(",");
        });
    });

    document.querySelectorAll("button[data-group='condiciones']").forEach(function(button) {
        button.addEventListener("click", function() {
            const valor = button.getAttribute("data-value");
            const index = condiciones.indexOf(valor);

            if (index === -1) {
                condiciones.push(valor);
                button.classList.add("selected");
            } else if (index !== -1) {
                condiciones.splice(index, 1);
                button.classList.remove("selected");
            }

            document.getElementById("condiciones").value = condiciones.join(",");
        });
    });
});
