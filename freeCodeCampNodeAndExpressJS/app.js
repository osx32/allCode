/*
const amount = 9;
if (amount < 10) {
    console.log('small number');
}
else {
    console.log('large number');
}
console.log(`hey it's my first node app!!!`);
*/


/*
// GLOBALS
// GLOBALS - NO WINNDOW !!!
// __dirname - path to current directory
// __filename - file name
// require - function to use modules (CommonJS)
// module - info abouut current module (file)
// process - info about env where the program is being executed
// console.log(__dirname);
setInterval(()=> {
    console.log('hello world');
}, 1000)
*/




// Modules
// CommonJS, every file is module (by default)
// Modules - Encapsulated Code (only share minimum)
const names = require('./4-names');
const sayHi = require('./5-utils');
const data=require('./6-alternative-flavor');
require('./7-mind-grenade');

//sayHi('susan');
//sayHi(names.john);
//sayHi(names.peter);
