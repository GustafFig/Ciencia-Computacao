/*
  na pasta raiz rode em background com
  node process.js &
  então confira o numero do process com
  ps | grep node
*/
console.log('Este processo tem o pid', process.pid);

setTimeout(() => {
  console.log('process to close');
}, 10000);
