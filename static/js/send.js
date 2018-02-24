/*
  Variáveis do arquivo inputs.js
  * input: possui o arquivo .csv a ser enviado
  * range_varv: valor v
  * range_faixas: quantidade de faixas
  * range_treino: porcentagem de dados para treino
  * enviar: botão de envio
*/

const URL = 'exec';

var formulario = document.getElementById('formulario');
formulario.action = URL;
formulario.method = "POST";

enviar.addEventListener('click', function() {
  /* 
    Se não tiver arquivo selecionado, não envia
  */
  if(input.files.length != 0) {
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', URL, true);
    xhttp.send();
  }
});
