/*
//The assert module provides a set of assertion functions for verifying invariants. The assert.deepStrictEqual()
// function tests for deep equality between the actual and expected parameters. If the condition is true it will
// not produce an output else an assertion error is raised.
//Requiring the module
const assert = require('assert').strict;
//Function call
try{
    assert.deepStrictEqual({a:1}, {a:'1'});
}
catch(error){
    console.log("Error: ", error);
}
*/


//Requiring the module
const assert = require('assert').strict;
//Function call
try{
    assert.deepStrictEqual({a:'5'}, {a:'5'});
    console.log('No Error Occurred')
}
catch(error){
    console.log('Error', error);
}