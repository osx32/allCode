/*Buffer The Buffer class is an inbuilt globally accessible class that means it can be used without importing any module. The Buffer class is used 
to deal with binary data. Buffer class objects are used to represent binary data as a sequence of bytes. 
*/ 
// const buffer = new Buffer(5, "abcde");
// console.log(buffer);



// console: It is an inbuilt global object used to print to stdout and stderr. 
// console.log('Hello World!!!');
// console.error('An error occured');



// process: It is an inbuilt global object that is an instance of EventEmitter
// used to get information on current process. It can also be accessed using 
// require() explicitly. 



//var myvar;
//console.log(typeof myvar);
//2.It is a global scope when declared within the browser. However, any variable defined within a node.js file is accessible only within that file.



/*setTimeout() method: It is a global function used to run a callback function after at least delay in milliseconds. Node.js does not guarantee the 
exact timing of when callbacks will fire but tries to maintain the timing as close as possible to the specified delay. Any delay larger than 2147483647 
or less than 1, is set to 1 automatically. Non-integer delays are truncated to the nearest integer. 

function printHello() {
    console.log('Hello World!');
}
//Now call above function after 2 seconds
var timeoutObj = setTimeout(printHello, 2000);
*/



/*TextEncoder: It is an implementation of the WHATWG Encoding Standard TextEncoder API. All instances of TextEncoder are encoded in UTF-8 only. 
*/
/*
const encoder = new TextEncoder();
const e = encoder.encode('Welcome to GFG');
console.log(e);


TextDecoder: It is an implementation of the WHATWG Encoding Standard TextDecoder API. 
const decoder = new TextDecoder();
const d = decoder.decode(e);
console.log(e);
*/


/*
// .Class: URL The URL class instance is a global object and is implemented by the following WHATWG URL Standard. The URL constructor creates a 
// new URL object as shown below. /foo is the input and https://www.helloworld.og/ is the base value. 

const url = new URL("/foo", "https://www.helloworld.og/");
console.log(url);
*/




/*
// URLSearchParams: URLSearchParams API is used to perform read and write operations on the query of a URL.
const myURL = new URL('http://www.registter.com/?name=gfg');
// It prints gfg
console.log(myURL.searchParams.get('name'));
myURL.searchParams.append('name', 'xyz');
// It prints http://www.register.com/?name=gfg&name=xyz
console.log(myURL.href);
*/



/*
// __dirname: The output throws an error which proves that __dirname is not globally defined in node.js. It requires a script to give the desired output as __dirname 
// is only defined in scripts. 
console.log(__dirname)
*/



// __filename: The output throws an error which proves that __filename is not globally defined in node.js. It requires a script to give the desired output as
// __filename is only defined in scripts. 
console.log(__filename);