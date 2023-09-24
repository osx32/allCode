
package car;
import java.util.*;
import org.w3c.dom.Text;

public class Car {

    
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        
        /*int []dizi1=new int[10];
        dizi1[0]=1;
        dizi1[1]=2;
        dizi1[2]=3;
        dizi1[3]=4;
        dizi1[4]=5;
        dizi1[5]=6;
        dizi1[6]=7;
        dizi1[7]=50;
        dizi1[8]=140;
        dizi1[9]=87;
         
        int k=0;
        for (int j = 0; j < 10; j++)
        {
            System.out.println("dizide eleman "+dizi1[k]);
            k++;
        }
        
        String sözcük="KaanFatihCoban";
        System.out.println(sözcük.indexOf("Coban"));
        
        System.out.println(11==10);
        */
        
        
        
        
        
        

        Araba TOG=new Araba();
        
        
        System.out.println("Arabanin beygirini gir ");
        int beygirDeg=input.nextInt();
        System.out.println("Id'si nedir");
        int IdDeg=input.nextInt();
        System.out.println("Arabanin motoru calisiyor mu true/false");
        boolean motorCalisiyorDeg=input.nextBoolean();
        System.out.println("Arabanin modelini gir ");
        TOG.model=input.nextInt();
        TOG.setBeygir(beygirDeg);
        TOG.setID(IdDeg);
        TOG.setMotorCalisiyor(motorCalisiyorDeg);
                
                
        System.out.println("Arabanin beygiri "+TOG.getBeygir());
        System.out.println("Arabanin ID'si "+TOG.getID());
        System.out.println("Arabanin motoru calisiyor mu "+TOG.getMotorCalisiyor());
        System.out.println("Arabanin modeli "+TOG.model);
        
        
        
  
    }
    
}
class Araba{
    
    
    private int beygir;
    private int Id;
    private boolean motorCalisiyor;
    public int model;
    
    public int getBeygir(){
        if (beygir<500)
        {
            System.out.println("beygir 500 altinda fazla dusuk");
        } 
        else
        {
            return this.beygir;
        }
        
        return this.beygir;
    }
    
    public boolean getMotorCalisiyor(){
        return this.motorCalisiyor;
    }
    
    public int getID(){
        return this.Id;
    }
    
    
    public void setBeygir(int beygir){
        this.beygir=beygir;
    }
    public void setID(int Id){
        this.Id=Id;
    }
    public void setMotorCalisiyor(boolean motorCalisiyor)
    {
        this.motorCalisiyor=motorCalisiyor;
    }
    
}

