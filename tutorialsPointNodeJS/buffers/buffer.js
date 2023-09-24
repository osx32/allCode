/*
var buff=new Buffer(10); 

var buff=new Buffer([10,20,30,40,50]);

var buff=new Buffer("Simply Easy Learning", "utf-8");

// buff.write(string[, offset][, length][, encoding]);

buf = new Buffer(256);
len =buf.write("Simply Easy Learning");
console.log("Octets written : "+ len);

buf = new Buffer(26);
for(var i=0;i<26;i++){
    buf[i]=i+97;
}
console.log(buf.toString('ascii'));          //outputs: abcdefghijklmnopqrstuvwxyz
console.log(buf.toString('ascii',0,5));      //outputs: abcde
console.log(buf.toString('utf-8',0,5));      //outputs: abcde
console.log(buf.toString(undefined,0,5));    //outputs: abcde

var buf=new Buffer('Simply Easy Learning');
var json=buf.toJSON(buf);
console.log(json);
*/

/*
var buffer1=new Buffer('TutorialsPoint');
var buffer2=new Buffer('Simply Easy Learning');
var buffer3=new Buffer.concat([buffer1,buffer2]);
console.log('buffer3 content: '+buffer3.toString());
*/

/*
var buffer1=new Buffer('ABC');
var buffer2=new Buffer('ABCD');
var result=buffer1.compare(buffer2);
if(result<0){
    console.log(buffer1+" comes before "+buffer2);
}else if(result===0){
    console.log(buffer1+" is same as "+ buffer2);
}else{
    console.log(buffer1+" comes after "+buffer2);
}
*/
