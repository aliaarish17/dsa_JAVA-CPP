package src;

import java.util.Scanner;

public class Maths {
    public static void main(String[] args) {
        int rev = 0;
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();

        while(n>0){
            int ld = n%10;
            rev = (rev*10)+ ld;
            n=n/10;
        
        }
        System.out.println(rev);
    }
}
