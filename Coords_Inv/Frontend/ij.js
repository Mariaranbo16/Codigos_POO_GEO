const tierra = document.getElementById("tierra");
const barraLateral = document.querySelector(".barra-lateral");
const spans = document.querySelectorAll(".menu-texto"); // Selecciona todos los elementos span con la clase menu-texto

tierra.addEventListener("click", () => {
    barraLateral.classList.toggle("mini-barra-lateral");

    spans.forEach((span) => {
        span.classList.toggle("oculto"); // Alterna la clase oculto para cada elemento span
    });
});
