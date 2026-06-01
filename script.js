const formulario = document.querySelector("form");
formulario.addEventListener("submit", function(event) {
  event.preventDefault();
  
  alert("¡Bienvenido a la constelación, viajero!");
});