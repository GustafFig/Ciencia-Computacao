const net = require('net');
const fs = require('fs');

const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin });

const server = net.createServer((socket) => {
  rl.on('line', (input) => socket.write(input));
  console.log('Connectado');
  socket.write('Olá cliente!!\n');
  socket.on('data', (data) => {
    console.log(data.toString());
  });
});

server.listen(8085);
