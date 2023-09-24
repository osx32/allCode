const html = require('http');
const port = 3000;
const host = '127.0.0.1';

const app = html.createServer((req,res) => {
    res.writeHead(200);
    res.write('Hello World, Never going back');
    res.end();
});

app.listen(port,host);