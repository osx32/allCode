// Defining local module: Local module must be written in a separate JavaScript file. In the separate file, 
// we can declare a JavaScript object with different properties and methods.
// Creating a local module with filename Welcome.js
const welcome = {
    sayHello: function() {
        console.log('Hello GeeksforGeeks user');
    },
    currTime: new Date().toLocaleDateString(),
    companyName:"GeeksforGeeks"
}
module.exports = welcome;