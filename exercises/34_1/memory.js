const os = require('os');

setInterval(() => {
  console.log('memoria usada', os.totalmem());
  console.log('memoria livre', os.freemem());
}, 1000);
