/*
// Creating a Hello World application using Node.js. Create a geeks.js file containing the following
// code:
console.log('Hello World');
*/



/*
//  Creating a Hello World application receiving the user input. Create a gfg.js file containing the 
// following code.
// The process.argv is used to provide command line argument to a program. Use
// the slice function with 2 as its argument to get all the elements of argv 
// that comes after its second element, i.e. the arguments the user entered The
// first argument is location of the Node.js binary which runs the program and
// the second argument is location of the file being run.
console.log(process.argv.slice(2));
*/



// Web-based Node.js Application
/*
Import required modules: Load Node.js modules using the require directive. Load 
http module and store returned HTTP instance into a variable.

Create server: Create a server to listen the client’s requests. Create server 
instance using createServer() method. Bind server to port 8080 using listen 
method associated with server instance.

Read request and return response: Read the client request made using browser 
or console and return the response. A function with request and response 
parameters is used to read client request and return response.
*/

// This example create a Hello World web-based application using Node.js. 
// Create a firstprogram.js file containing the following code.
//Require http header
var http = require('http');
//Create server
http.createServer(function (req, res) {
    //HTTP Status: 200 : OK
    //Content Type: text/html
    res.writeHead(200, {'Content-Type': 'text/html'});
    //Send the response body as 'Hello World'
    res.end('Hello World');
}).listen(8080);

