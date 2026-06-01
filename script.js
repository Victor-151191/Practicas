const formulario = document.querySelector("form");
formulario.addEventListener("submit", function(event) {
  event.preventDefault();
  
  formulario.innerHTML = "¡Gracias por unirte a la constelacion!";
  
});

