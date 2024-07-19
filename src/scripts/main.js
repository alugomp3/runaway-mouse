document.addEventListener('DOMContentLoaded', function() {
    const sim = document.getElementById("optnYes");
    const nao = document.getElementById("optnNo");

    nao.addEventListener("mouseenter", moveNoButton);
    sim.addEventListener("click", function() {
        location.href = "https://www.youtube.com/watch?v=orWnzqBA63w";
    });

    function moveNoButton() {
        const container = document.querySelector('.container');
        const containerRect = container.getBoundingClientRect();
        const buttonRect = nao.getBoundingClientRect();

        // Define o limite de movimento em pixels
        const limit = 500;

        // Garante que o botão não ultrapasse o limite de 1000px e se mantenha visível
        const maxX = Math.min(containerRect.width - buttonRect.width, limit);
        const maxY = Math.min(containerRect.height - buttonRect.height, limit);

        // Gera posições aleatórias dentro do limite definido
        const randomX = Math.random() * maxX;
        const randomY = Math.random() * maxY;

        // Ajusta a transformação para a posição aleatória
        nao.style.transform = `translate(${randomX}px, ${randomY}px)`;
    }
});