/*
// The JavaScript for in statement loops through the properties of an Object:
const person = { fname: 'John', lname: 'Doe', age: 25 };
let text = '';
for (let x in person) {
    text += person[x];
}
console.log(text);
*/

/*
The for in loop iterates over a person object
Each iteration returns a key (x)
The key is used to access the value of the key
The value of the key is person[x]
*/



/*
// For In Over Arrays
// The JavaScript for in statement can also loop over the properties of an Array:
const numbers = [45, 4, 9, 16, 25];
let txt = "";
for (let x in numbers) {
    txt += numbers[x];
}
console.log(txt);
*/
// Do not use for in over an Array if the index order is important.


// Array.forEach()
// The forEach() method calls a function (a callback function) once for each array element.
const numbers = [45, 4, 9, 26, 25];
let txt = "";
numbers.forEach(myFunction);
function myFunction(value, index, array) {
    txt += value;
}
console.log(txt);