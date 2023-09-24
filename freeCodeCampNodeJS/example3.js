const events=require('events');
const myEmitter=new events.EventEmitter();
myEmitter.on('status',(code,msg)=>console.log(`Got ${code} and ${msg}`));
myEmitter.emit('status', 200, 'ok');
