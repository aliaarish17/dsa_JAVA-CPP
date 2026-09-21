package src;
import java.util.*;

public class Array {

    public static void main(String[] args) {
        int arr[] = new int[5];// declaration and allocation
        int brr [] = {10,20,30}; // initialisation

        // System.out.println("value at 0th index"+brr[0]); // accessing

        //for loop to access:

        // int n = brr.length;

        // for(int i=0; i<=n-1;i++){
        //     System.out.println(brr[i]);
        // }


        //ForEach loop:

        for(int val: brr){
            System.out.println(val);
        }
 
    }
}