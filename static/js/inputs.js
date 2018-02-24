/* Input de arquivos*/
var input = document.getElementsByName('database')[0];
/* Label que fica por cima do input de arquivos*/
var span = document.getElementsByTagName('label')[0].children[1];

input.addEventListener('change', function() {
  if(this.files.length == 0){
    span.classList.remove('withFile');
  }
  else{
    /* Pega o arquivo e exibe as informações sobre ele*/
    var file = this.files[0];
    var name = file.name;
    var size = (file.size / 1048576).toFixed(3);
    /* Remove o estilo caso tenha sido adicionado*/
    span.style.color = '';
    /* Adiciona essa classe, para deixar o texto mais escuro*/
    span.classList.add('withFile');
    span.textContent = name + ' (' + size + 'mb)';
  }
});

/* Pega a legenda: Opções Avançadas*/
var legend = document.getElementsByTagName('legend')[0];
/* Pega o triangulo */
var svgTriangle = legend.children[0];
/* Pega a div 'avancados' que fica oculta por padrão*/
var avancedOptions = document.getElementById('avancados');
/* Evento de clique*/
legend.addEventListener('click', function() {
  /* variável para manipular a exibição do elemento*/
  var display = avancedOptions.style.display;
  if(display == '') {
    /* 
      Se estiver oculto:
      * exibe as opções avançadas
      * rotaciona o triângulo
    */
    avancedOptions.style.display = 'block';
    svgTriangle.style.transform = 'rotate(180deg)';
    svgTriangle.style.webkitTransform = 'rotate(180deg)';
  } else {
    /* 
      Se não estiver oculto:
      * oculta as opções avançadas
      * não rotaciona o triângulo
    */
    avancedOptions.style.display = '';
    svgTriangle.style.transform = '';
    svgTriangle.style.webkitTransform = '';
  }
});

/* Elementos relacionados aos inputs do tipo range*/
var range_varv = document.getElementsByName('varv')[0];
var range_faixas = document.getElementsByName('faixas')[0];
var range_treino = document.getElementsByName('treino')[0];
var varv = document.getElementById('varv');
var faixas = document.getElementById('faixas');
var treino = document.getElementById('treino');

/*
  Pega os valores padrões dos inputs
  Adiciona eles aos spans para melhor experiência de usuário
*/
varv.innerHTML = range_varv.value;
faixas.innerHTML = range_faixas.value;
treino.innerHTML = range_treino.value;

/* Modifica o valor do span a cada mudança no valor do input*/
range_varv.addEventListener('change', function() {
  varv.innerHTML = this.value;
});

range_faixas.addEventListener('change', function() {
  faixas.innerHTML = this.value;
});

range_treino.addEventListener('change', function() {
  treino.innerHTML = this.value;
});

/* Botão submit: id = enviar*/
var enviar = document.getElementById('enviar');
enviar.addEventListener('click', function() {
  /* 
    Se não tiver arquivo selecionado
    Exibir o texto do span em vermelho
  */
  if(input.files.length == 0) {
    span.style.color = '#f44336';
  }
});