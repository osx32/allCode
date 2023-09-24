#!/usr/bin/env node
/*
// Loose Typing: Node.js supports loose typing, it means you
// don’t need to specify what type of information will be stored
// in a variable in advance. We use var keyword in Node.js to
// declare any type of variable. Examples are given below:
// Variable store number data type
var a = 35;
console.log(typeof a);

//Variable store string data type
a = "GeeksforGeeks";
console.log(typeof a);

//Variable store Boolean data type
a = true;
console.log(typeof a);

// Variable store undefined (no value) data type
a = undefined;
console.log(typeof a);
*/



/*
// Objects & Functions: Node.js objects are same as JavaScript objects i.e. 
// the objects are similar to variable and it contains many values which are
//  written as name : value pairs. Name and value are separated by colon and
// every pair is separated by comma.
var company  = {
    Name: "GeeksforGeeks",
    Address: "Noida",
    Contact: "+905305644134",
    Email:"abc@example.com"
};
//Dispaly the object information
console.log("Information of variable company:", company);
//Display the type of variable
console.log("Type of variable company:", typeof company);
*/



/*
// Node.js functions are defined using function keyword then the name of the
// function and parameters which are passed in the function. In Node.js, we don’t
// have to specify datatypes for the parameters and check the number of 
// arguments received. Node.js functions follow every rule which is there while
// writing JavaScript functions.
function multiply(num1, num2) {
    // It returns the multiplication
    // of num1 and num2
    return num1 * num2;
}
// Declare variable
var x = 2;
var y = 3;
// Display the answer returned by
// multiply function
console.log("Multiplication of", x,
        "and", y, "is", multiply(x, y));
*/



/*
// String and String Functions: In Node.js we can make a variable as string by 
// assigning a value either by using single (”) or double (“”) quotes and it contains
// many functions to manipulate to strings.
// Following is the example of defining string variables and functions in node.js.
var x = "Welcome to GeeksforGeeks ";
var y = 'Node.js Tutorials';
var z = ['Geeks', 'for', 'Geeks'];
console.log(x);
console.log(y);
console.log("Concat Using (+) :", (x + y));
console.log("Concat Using Function :", (x.concat(y)));
console.log("Split string: ", x.split(' '));
console.log("Join string: ", z.join(', '));
console.log("Char At Index 5: ", x.charAt(5));
*/



/*
// Buffer: In node.js, we have a data type called “Buffer” to store a binary data and
// it is useful when we are reading a data from files or receiving a packets over network.
// Node.js console-based application: Make a file called console.js with the following code.
console.log('Hello this is the console-based application');
console.log('This all will be printed in console');
*/



// Node.js web-based application: Node.js web application contains different
// types of modules which is imported using require() directive and we have to
// create a server and write code for the read request and return response.
// Make a file web.js with the following code.

// Require http module
var http = require('http');
// Create server
http.createServer(function (req, res){
    //Send the HTTP header
    //HTTP Status: 200 : OK
    //Content Type: text/plain
    res.writeHead(200, {'Content-Type': 'text/plain'});

    //Send the response body as "This is the example"
    //of node.js web based application
    res.end('This is the example of node.js web-based application \nHello World');

//Console will display the message
}).listen(5000, ()=>console.log('Server running at http://127.0.0.1:5000/'));