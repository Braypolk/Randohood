const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 8080

app.use(express.static(__dirname +'/static/'));
app.use(bodyParser.urlencoded({ extended: false }));

app.get('/', (req, res) => res.sendFile(`${__dirname}/templates/index.html`));

app.post('/api/data', function(req, res){
    console.log(req.body)
    var credentials = {
        username: 'braypolk@comcast.net',
        password: 'Bray89511!'
    }
    var Robinhood = require('robinhood')(credentials, function(){

    //Robinhood is connected and you may begin sending commands to the api.

    Robinhood.quote_data('GOOG', function(error, response, body) {
        if (error) {
            console.error(error);
            process.exit(1);
        }
        console.log(body);
    });

});
    res.end()
});

function updateValues(){
    document.getElementById('purchasedAmount').innerHTML = `You Purchased ${dollarAmountPurchased} worth of`;
    document.getElementById('randomStock').innerHTML = `${randomStock}`;
    document.getElementById('purchasePrice').innerHTML = `\$${purchasePrice}`;
    document.getElementById('dollarAmountPurchased').innerHTML = `Just reload the page to "invest" another ${dollarAmountPurchased}`;
}

app.listen(port, () => console.log(`App listening at http://localhost:${port}`))