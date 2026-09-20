import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int a = input.nextInt();

        input.nextLine(); // consumes \n

        String b = input.nextLine(); // consumes Aarish Ali\n
        boolean c = input.nextBoolean();

        System.out.println(a+" "+ b + " "+ c);
    }
}