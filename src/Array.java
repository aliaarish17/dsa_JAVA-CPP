package src;
import java.util.*;

public class Array {

    public static void main(String[] args) {
        int arr[] = {10,20};
        int n = arr.length;
        int product = 1;
        System.out.println("product of elements of array");
        
        for(int i=0; i<=n-1;i++){
            product*=arr[i];
            
        }  
        System.out.println(product);
    }
}