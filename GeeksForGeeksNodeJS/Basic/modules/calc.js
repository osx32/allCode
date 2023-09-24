// Local Modules: Unlike built-in and external modules, local modules are created locally in your Node.js
// application. Let’s create a simple calculating module that calculates various operations. Create a calc.js
// file that has the following code:
exports.add = function(x, y) {
    return x+y;
};
exports.sub = function(x, y) {
    return x-y;
};
exports.mult = function(x, y){
    return x*y;
};
exports.div = function(x, y) {
 return x/y;   
}