var events = require('events');
const { EventEmitter } = require('stream');
var eventEmmitter=new events.EventEmitter();
EventEmitter.on('eventName',eventHandler);
EventEmitter.emit('eventName');
