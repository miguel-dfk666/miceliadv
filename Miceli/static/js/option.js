document.addEventListener("DOMContentLoaded", function () {
  const opcaoSelect = document.getElementById("opcao");
  const opcaoInput = document.getElementById("opcao_input");

  // Evento de mudança na caixa de seleção
  opcaoSelect.addEventListener("change", function () {
    const selectedOption = opcaoSelect.value;
    opcaoInput.innerHTML = ""; // Limpa o conteúdo anterior

    // Adiciona o campo de entrada específico com base na opção selecionada
    if (selectedOption === "numero_processo") {
      opcaoInput.innerHTML = '<label for="input_numero_processo">Número de Processo:</label>' +
        '<input type="text" name="input_numero_processo" id="input_numero_processo" class="w-full px-4 py-2 mt-2 border rounded-lg" pattern="[0-9]{7}-[0-9]{2}.[0-9]{4}.[0-9].[0-9]{2}.[0-9]{4}" placeholder="Exemplo: 0000000-00.0000.0.00.0000" required>';
    } else if (selectedOption === "numero_oab") {
      opcaoInput.innerHTML = '<label for="input_numero_oab">Número OAB:</label>' +
        '<input type="text" name="input_numero_oab" id="input_numero_oab" class="w-full px-4 py-2 mt-2 border rounded-lg" pattern="[A-Za-z0-9]*" placeholder="Exemplo: ABC12345" required>';
    } else if (selectedOption === "data_abertura") {
      opcaoInput.innerHTML = '<label for="input_data_abertura">Data de Abertura:</label>' +
        '<input type="date" name="input_data_abertura" id="input_data_abertura" class="w-full px-4 py-2 mt-2 border rounded-lg" required>';
    }
  });
});
