var pass = readline();
var rh = require('robinhood')({username: 'braypolk@comcast.net', password: pass}, function(){
    rh(null).quote_data('GOOG', function(error, response, body) {
        if (error) {
            console.error(error);
            process.exit(1);
        }

        console.log(body);
    });
});