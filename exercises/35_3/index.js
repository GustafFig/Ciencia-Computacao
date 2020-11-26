const express = require('express');

const app = express()

app.use('/', express.static('images'));

PORT = 3000;

app.listen(PORT, () => console.log(`Ouvindo na porta ${PORT}`));
