const os = require('os');

console.log('Está na plataforma', os.platform(), '; arquitetura:', os.arch(), '; lançada', os.release());

const cores = os.cpus();
console.log('o computador usa', cores.length, 'cores, com velocidades', ...cores.map(({ speed }) => `${speed / 1000}GHz`));

console.log('memoria usada', `${Math.floor(os.totalmem() / 1024 / 1024)}MB`);
console.log('memoria livre', `${Math.floor(os.freemem() / 1024 / 1024)}MB`);

