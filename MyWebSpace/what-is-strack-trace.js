/*
console.log('This program demonstrates'+'stack trace in Node.js');
var err = new Error().stack
console.log(err);
*/

/*
const obj = {};
Error.captureStackTrace(obj);
console.log(obj.stack);
*/


/*
//Alternatively
function MyNewError()
{
    Error.captureStackTrace(this, MyNewError);
}
console.log(new MyNewError().stack);
*/


/*
try{
    throw new Error('Error occured');
}
catch(e){
    console.log(e);
}
*/



//console.trace('Hello World');

/*
try{
    throw new Error('Custom Error');
}
catch(error){
console.log(error);
}
*/

/*
try{
    throw new Error('Error occured');
}
catch(s){
    console.log(s);
}
*/

//console.log(new Error('custom error'.stack));


const myemp =
    {
    id:11, 
    name:'Eric'
    };
Error.captureStackTrace(myemp);
console.log(myemp.stack);