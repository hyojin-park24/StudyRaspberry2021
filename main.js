// javascript Node.js
var http = require('http'); // http모듈을 가져다 쓰겠다는 의미
http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type' : 'text/plain'});      //web에서 200 = ok (웹열겠다는 의미)
    res.end('Hello Univers\n');
}).listen(8080, '127.0.0.1');        //port : 8080 , host : 127.0.0.1
console.log('Server is running at http://127.0.0.1:8080/');