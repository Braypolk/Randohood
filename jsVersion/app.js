const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000

app.get('/', (req, res) => res.sendFile(`${__dirname}/templates/index.html`))

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))