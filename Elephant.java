import java.util.Scanner;

public class Elephant {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int steps = sc.nextInt;
        int x = 5;
        int count = 0 ;
        while(steps>0){
            steps-=x;
            count++;
            if(steps < x){
                x--;
            }
        }
        System.out.println(count);
    }
}
