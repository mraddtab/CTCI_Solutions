import java.util.Arrays;

public class arrays {
    static boolean isUnique(String str){
        boolean ascii_table[] = new boolean[128];
        Arrays.fill(ascii_table, false);
        for(int i = 0; i < str.length(); i++){
            char curr_char = str.charAt(i);
            if(ascii_table[curr_char] == true){
                return false;
            }
            else{
                ascii_table[curr_char] = true;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        String test = "Hello";
        System.out.println(isUnique(test));
    }
}
