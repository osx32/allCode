const events=require('events');
const myEmitter=new events.EventEmitter();
myEmitter.once('eventOnce',()=>console.log('eventOnce once fired'));
myEmitter.emit('eventOne');