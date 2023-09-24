
package javaapplication1;


public class JavaApplication1 {

    String miraba="miraba";
    public static void main(String[] args) {
        System.out.println("sa");
        
        methodum("tur");
        methodlar("kaan", 19);
        checkAge(19);
        int ilknum=plusMethod(10, 20);
        double secnum=plusMethod(25, 15);
        System.out.println("int olan :"+ilknum+"double olan :"+secnum);
        int result=sum(10);
        System.out.println(result);
        int result2=sum2(5, 10);
        System.out.println(result2);
        Araba firstaraba=new Araba();
        Araba secaraba=new Araba();
        System.out.println(firstaraba.color);
        System.out.println(firstaraba.x);
    }
    static void methodum(String kelime){
        System.out.println("kelimeniz "+kelime);
    }
    public static void methodlar(String fname,int age){
        System.out.println(fname+" is "+age);
    }
    static void checkAge(int age){
        if(age<18){
            System.out.println("Access denied - You are not old enough!");
        }
        else{
            System.out.println("Access granted - You are old enough!");
        }
    }
    static int plusMethod(int x,int y){
        return x+y;
    }
    static double plusMethod(double x,double y){
        return x+y;
    }
    public static int sum(int k){
        if(k>0){
            return k+sum(k-1);
        }
        else{
            return 0;
        }
    }
    public static int sum2(int start ,int end){
        if (end>start){
            return end+sum2(start,end-1);
            
        }
        else{
            return end;
        }
    }
        
}
