import java.util.Scanner;

public class Soldier_and_Bananas {
    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        String userInput = s.nextLine();
        String[] arr = userInput.split("\\s+");
        int NumbOfB = Integer.parseInt(arr[2]);
        int total = 0 ;
        for (int i = 1; i <= NumbOfB; i++) {
            total+= i*Integer.parseInt(arr[0]);
        }
        if(Integer.parseInt(arr[1])>=total){
            System.out.println(0);
        }else{
            System.out.println(total-Integer.parseInt(arr[1]));
        }
        
    
    }
}
