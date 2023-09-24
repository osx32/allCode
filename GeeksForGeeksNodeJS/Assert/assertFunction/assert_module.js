// Assert module in Node.js provides a bunch of facilities that are useful for the assertion of the function.
// The assert module provides a set of assertion functions for verifying invariants. If the condition is true it 
// will output nothing else an assertion error is given by the console.
/*console.clear();
const assert = require('assert');
let x = 4;
let y = 5;
try {
    //Checking condition
    assert(x == y);
}
catch{
    //Error output
    console.log(`${x} is not equal to ${y}`);
}
*/


// Note: In this example, no try-catch is given so an assertion error of the kind given 
// below will be the output.
console.clear();
const assert = require('assert');
let x = 4;
let y = 5;
assert(x > y);