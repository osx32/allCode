/*
var http = require('http');
// Create a server object:
http.createServer(function (req, res) {
    //Write a response to the client
    res.write('GeeeksForGeeks');
    // End the response 
    res.end();
    // The server object listens on port 8080
}).listen(8080);
*/


var events = require('events');
var eventEmitter = new events.EventEmitter();
// Create an event handler:
var myEventHandler = function () {
    console.log('Welcome to GeeksforGeeks');
}
// Assign the event handler to an event:
eventEmitter.on('geeks', myEventHandler);
// Fire the 'geeeks' event:
eventEmitter.emit('geeks');


