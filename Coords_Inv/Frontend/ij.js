const tierra = document.getElementById("tierra");
const barraLateral = document.querySelector(".barra-lateral");
const spans = document.querySelectorAll(".menu-texto");

tierra.addEventListener("click", () => {
    barraLateral.classList.toggle("mini-barra-lateral");

    spans.forEach((span) => {
        span.classList.toggle("oculto");
    });
});
