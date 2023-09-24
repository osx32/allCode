/*
// Requiring the module
const assert = require('assert').strict;
//Function call
try{
    assert(0);
}
catch(error)
{
    console.log("Error:", error);
}
*/



// Requiring the module
const assert = require('assert').strict;
//Function call
try{
    assert(0);
    console.log("No Error Occurred");
}
catch(error){
    console.log("Error:", error);
}