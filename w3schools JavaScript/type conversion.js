// JavaScript variables can be converted to a new variable and another data type:
//By the use of a JavaScript function
//Automatically by JavaScript itself


/*
//Converting Strings to Numbers
The global method Number() converts a variable (or a value) into a number.
A numeric string (like "3.14") converts to a number (like 3.14).
An empty string (like "") converts to 0.
A non numeric string (like "John") converts to NaN (Not a Number).

console.log(Number("3.14"));
console.log(Number(Math.PI));
console.log(Number(""));
console.log(Number(""));
*/


/*
//These will not convert:
console.log(Number("99 88"));
console.log(Number("John"));
*/





// Number MEthods
//Number()	Returns a number, converted from its argument
//parseFloat()	Parses a string and returns a floating point number
//parseInt()	Parses a string and returns an integer





/*
// The Unary + Operator
// The unary + operator can be used to convert a variable to a number:
let y = "5";  // y is a string
let x = + y;  // x is a number
console.log(typeof y);
console.log(typeof x);
*/

/*
// If the variable cannot be converted, it will still become a number, but with the value NaN (Not a Number):
let y = "John"; // y is a string
let x = + y;    // x is a number(NaN)
console.log(typeof y);
console.log(typeof x);
console.log(x);
*/



/*
// Converting Numbers to Strings
// The global method String() can convert numbers to strings.
// It can be used on any type of numbers, literals, variables, or expressions:
let x = 5;
console.log(String(x));  // returns a string from a number variable x
console.log(String(123));  // returns a string from a number literal 123
console.log(String(100 + 23));  // returns a string from a number from an expression
console.log(typeof String(123));

// The Number method toString() does the same.
console.log(x.toString());
console.log((123).toString());
console.log((100 + 23).toString());
console.log(typeof x.toString());
*/




// More Methods
// toExponential()	Returns a string, with a number rounded and written using exponential notation.
// toFixed()	Returns a string, with a number rounded and written with a specified number of decimals.
// toPrecision()	Returns a string, with a number written with a specified length



/*
// Converting Dates to Numbers
// The global method Number() can be used to convert dates to numbers.
d = new Date();
console.log(Number(d));   // returns 1677089448311
// The date method getTime() does the same.
d = new Date();
console.log(d.getTime());
*/



/*
// Converting Dates to Strings
// The global method String() can convert dates to strings.
console.log(String(Date()));   //returns Wed Feb 22 2023 21:13:54 GMT+0300 (GMT+03:00)
// The Date method toString() does the same
console.log(Date().toString());  // returns Wed Feb 22 2023 21:14:48 GMT+0300 (GMT+03:00)
*/





/*
// Converting Booleans to Numbers
// The global method Number() can also convert booleans to numbers
console.log(Number(false));  // returns 0
console.log(Number(true))  // returns 1
*/



/*
// Converting Booleans to Strings
// The global method String() can convert booleans to strings.
console.log(String(false));   // returns "false"
console.log(typeof String(false));
console.log(String(true));    // returns "true"
// The Boolean method toString() does the same.
console.log(false.toString()); // returns "false"
console.log(typeof false.toString());
console.log(true.toString());  // returns "true"
*/




/*
// Automatic Type Conversion
// When JavaScript tries to operate on a "wrong" data type, it will try to convert the value to a "right" type.
// The result is not always what you expect:
console.log(5 + null);  // returns 5         because null is converted to 0
console.log("5" + null);// returns "5null"   because null is converted to "null"
console.log("5" + 2);  // returns "52"      because 2 is converted to "2"
console.log("5" - 2);  // returns 3         because "5" is converted to 5
console.log("5" * "2");  //  returns 10        because "5" and "2" are converted to 5 and 2
*/



/*
// Automatic String Conversion
// JavaScript automatically calls the variable's toString() function when you try to "output" an object or a variable:
document.getElementById().innerHTML = myVar;
// if myVar = {name:"Fjohn"}  // toString converts to "[object Object]"
// if myVar = [1,2,3,4]       // toString converts to "1,2,3,4"
// if myVar = new Date()      // toString converts to "Fri Jul 18 2014 09:08:55 GMT+0200"
*/



// Numbers and booleans are also converted, but this is not very visible:
// if myVar = 123             // toString converts to "123"
// if myVar = true            // toString converts to "true"
// if myVar = false           // toString converts to "false"











