/*
var events = require('events');

var eventEmitter=new events.EventEmitter();

var connectHandler =function connected(){
    console.log('connection succesful');
    eventEmitter.emit('data_received');
}

eventEmitter.on('connection', connectHandler);

eventEmitter.on('data_received',function(){
    console.log('data received succesfully');
});

eventEmitter.emit('connection');

console.log('Program Ended');
*/



var fs=require('fs');
fs.readFile('input.txt',function(err, data){
    if(err){
        console.log(err.stack);
        return;
    }
    console.log(data.toString());
});
console.log('Program Ended');
