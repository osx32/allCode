const http = require('http');
const host='127.0.0.1';
const port = 3000;
const app = http.createServer((req,res)=>{
    res.writeHead(200,'Content-Type:text/plain');
    res.end('Helo World');
});
app.listen(port,host);