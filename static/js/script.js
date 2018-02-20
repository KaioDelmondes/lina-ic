var input = document.getElementsByName('database')[0];
var span = document.getElementsByTagName('label')[0].children[1];

input.addEventListener('change', function() {
  if(this.files.length == 0){
    span.classList.remove('withFile');
  }
  else{
    var file = this.files[0];
    var name = file.name;
    var size = (file.size / 1048576).toFixed(3);
    span.classList.add('withFile');
    span.textContent = name + ' (' + size + 'mb)';
  }
});

var legend = document.getElementsByTagName('legend')[0];
var avanced_options = document.getElementById('avancados');
legend.addEventListener('click', function() {
  var display = avanced_options.style.display;
  if(display == '') {
    avanced_options.style.display = 'block';
  } else {
    avanced_options.style.display = '';
  }
});