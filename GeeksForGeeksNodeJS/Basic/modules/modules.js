// Core Modules: Node.js has many built-in modules that are part of the platform and comes with Node.js installation.
// These modules can be loaded into the program by using the require function.
// var module = require('modeule_name');




// The require() function will return a JavaScript type depending on what the particular module returns. The following
// example demonstrates how to use the Node.js Http module to create a web server.
var http = require('http');
http.createServer(function(req, res){
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('Welcome to this page!');
    res.end();
}).listen(2999);