import java.util.Scanner;

public class Bear_and_Big_Brother {
    public static void main(String[] args) {
        Scanner Sca = new Scanner(System.in);
        int me = Sca.nextInt();
        int bro = Sca.nextInt();
        int count = 0 ;
        while(me<=bro){
            me*=3;
            bro*=2;
            count++;
        }
        System.out.println(count);
    }
}
