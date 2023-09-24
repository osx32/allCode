const port = 3000;
const host = '127.0.0.1';
const http = require('http');
var app = http.createServer((req,res)=>{
    res.writeHead(200,'Context-Type','text/plain');
    res.end('Hello World!');
});

app.listen(port,host);