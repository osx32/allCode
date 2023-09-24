/*
function greet(name, callback){
    console.log('Hi' + ' ' + name);
    callback();
} 

function callMe(){
    console.log('I am callback function');
}

greet('Peter', callMe);
*/


/*
function greet(name, myFunction){
    console.log('Hello World');
    myFunction(name);
}

function sayName(name){
    console.log('Hello ' + name);
}
setTimeout(greet, 2000, 'John', sayName);
*/

/*
function sup(name,callBack,rythm){
    callBack();
    console.log(`Hi ${name}`);
    rythm();
}

function callLater(){
    console.log('Hey Jim, Jeremy, Jimothy, Tuna');
}

function rythm(){
    console.log('Tuna rididip diditdut dudu');
}

sup('Jim',callLater,rythm);
*/


/*
function end(bottom){
    console.log(`End of the code, result is: ${bottom}`);
}

function office(name,end){
    console.log(`Hi ${name}`);
    end('Bear, Beets, BattleStar Galactica');
}

office('Dwight', end);
*/

/*
function quote(end){
    console.log(`Final word: goodbye and ${end}`);
}

function office(name,callBack){
    console.log(`Hello ${name}`);
    callBack('Thats what she said');
}

office('Pam', quote);
*/

function callBack(){
    console.log('We back');
}

function mainFunc(callBack){
    console.log("Hello World I'm main function");
    callBack();
}
mainFunc(callBack);