
package Device;

import java.util.*;
public class Device {

    
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        Cihaz switch1=new Cihaz();
        System.out.println("anahtarlayicinin MAC adresi : " );
        switch1.macAdres=input.nextInt();
        System.out.println("anahtarlayıcının ip numarasi ");
        switch1.ip=input.nextInt();
        switch1.maxSpeed=8;
        System.out.println("anahtarlayıcının maximum hizi "+switch1.maxSpeed);
        System.out.println("anahtarlayıcının cihaz adi(marka ismi)");
        switch1.cihazAd=input.next();
        System.out.println("anahtarlayicinin su anki kanali");
        switch1.channel=(char) input.nextInt();
    }
    
}
class Cihaz{
    int macAdres;
    int ip;
    int maxSpeed;
    String cihazAd;
    char channel;
    private String webSite;
    
    public void setWEBSİTE(String webSite)
    {
        this.webSite=webSite;
    }
    public String getWEBSİTE()
    {
        return webSite;
    }
}






