/* Endpoints para execução dos algoritmos*/
const URL = {
  home : '/',
  exec : 'exec'
};

/* Recuperar o formulário, definir a ação e o método*/
var formulario = document.getElementById('formulario');
formulario.action = URL.exec;
formulario.method = 'POST';
formulario.enctype = 'multipart/form-data';
