const dgram = require('dgram');
const readline = require('readline');

const socket = dgram.createSocket('udp4', { port: 8086 });
const rl = readline.createInterface({ input: process.stdin });

socket.on('message', (message, rinfo) => {
  console.log(`${rinfo}
  ${message.toString()}`);
  rl.on('line', (input) => socket.send(input));
});

socket.on('listening', () => {
  console.log('Conectado!!');
});

socket.bind(8086);
