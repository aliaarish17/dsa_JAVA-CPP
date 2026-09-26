;

public class Solution {
    String rveString(String s){
    s = s.trim();
    String reverse ="";
    String[] arr = s.split("\\s+");
    for(int i = arr.length-1; i>=0; i--){
        if(reverse.length()>0){
            reverse= reverse+" ";
        }
        reverse=reverse+arr[i];
    }
    return reverse;

    
}
}
