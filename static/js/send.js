/* Endpoints para execução dos algoritmos*/
const URL = {
  home : '/',
  exec : 'exec',
  upload : 'upload'
};

/* Recuperar o formulário, definir a ação e o método*/
var formulario = document.getElementById('formulario');

/* Remover o evento padrão de submissão do formulário */
formulario.addEventListener('submit', function(event) {
  event.preventDefault();
});

/*
  Botão submit: id = enviar
  Onclick: Verifica se o arquivo já foi selecionado.
  Se sim, faz upload do arquivo.
  Se não, destaca em vermelho o campo de seleção de arquivo.
*/
var enviar = document.getElementById('enviar');
enviar.addEventListener('click', function() {
  if(input.files.length == 0) {
    span.style.color = '#f44336';
  } else {
    upload_file();
  }
});

/*
  Método responável por fazer o upload do arquivo
  Cria um objeto FormData.
  Adiciona o arquivo selecionado nesse objeto.
  Faz uma requisição ao servidor:
    Método: POST
    Content-Type: multipart/form-data
  Em caso de sucesso:
    Recebe como resposta do servidor o nome do arquivo
    Executa o método exec(nome do arquivo).
*/
function upload_file() {
  var formData = new FormData();
  formData.append('file', input.files[0]);
  axios.post(URL.upload, formData, { headers : { 'Content-Type' : 'multipart/form-data' } })
    .then(function(response) {
      console.log(response.data);
      var filename = response.data;
      exec(filename);
    });
}

/*
  Método responsável por enviar os dados do formulário ao servidor.
  Parâmetro:
    filename: nome do arquivo que veio como resposta da requisição anterior.
  Cria um objeto FormData.
  Seleciona todos campos inputs e selects dentro do formulário.
  Adiciona ao objeto FormData os valores dos campos selecionados.
    { nome_do_campo, valor_do_campo}
    OBS: Não seleciona o input de arquivo e o botão submit
  Adiciona o nome do arquivo ao objeto FormData.
  Faz uma requisição ao servidor:
    Método: POST
    Content-Type: multipart/form-data
  Em caso de sucesso:
    Recebe os dados da execução dos algoritmos.
*/
function exec(filename) {
  var formData = new FormData();
  var allInputs = formulario.getElementsByTagName('input');
  var allSelections = formulario.getElementsByTagName('select');
  for(var i = 0; i < allInputs.length; i++) {
    if(allInputs[i].name !== 'database' && allInputs[i].name !== '') {
      formData.append(allInputs[i].name, allInputs[i].value);
    }
  }
  for(var i = 0; i < allSelections.length; i++) {
    formData.append(allSelections[i].name, allSelections[i].value);
  }
  formData.append('filename', filename);
  axios.post(URL.exec, formData, { headers : { 'Content-Type' : 'multipart/form-data' } })
    .then(function(response) {
      console.log(response.data);
    });
}