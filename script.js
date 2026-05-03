function adicionarTarefa() {
  const input = document.getElementById("inputTarefa");
  const texto = input.value;

  if (texto === "") {
    alert("Digite uma tarefa!");
    return;
  }

  const lista = document.getElementById("lista");

  const item = document.createElement("li");
  item.textContent = texto;

  // Marcar como concluída
  item.onclick = function () {
    item.classList.toggle("concluida");
  };

  // Remover com duplo clique
  item.ondblclick = function () {
    lista.removeChild(item);
  };

  lista.appendChild(item);
  input.value = "";
}