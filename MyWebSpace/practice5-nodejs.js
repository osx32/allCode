const http = require('http');

const port = 3000;
const host = '128.0.0.1';

const app = http.createServer((req,res) => {
    res.writeHead(200,'Content-Type','text/plain');
    res.end('Hell yess');

})
app.listen(port,host);