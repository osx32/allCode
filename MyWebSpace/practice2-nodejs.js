const http = require('http');
const port = 3000;
const host = '127.0.0.1';
const app = http.createServer((req,res){
    res.writeHead('Content-Type','text/plain');
    res.end('Hello World');
})
app.listen(port,host);