document.addEventListener("DOMContentLoaded", function () {
  const dropdownButton = document.getElementById("profile-dropdown-button");
  const dropdownMenu = document.getElementById("profile-dropdown-menu");

  dropdownButton.addEventListener("click", function () {
      dropdownMenu.classList.toggle("hidden");
  });

  // Fechar o menu se o usuário clicar fora dele
  document.addEventListener("click", function (event) {
      if (!dropdownButton.contains(event.target)) {
          dropdownMenu.classList.add("hidden");
      }
  });

  // Evitar o fechamento do menu se o usuário clicar no botão
  dropdownButton.addEventListener("click", function (event) {
      event.stopPropagation();
  });
});