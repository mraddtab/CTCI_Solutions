import java.util.Arrays;
import java.lang.Math;
import java.util.HashMap;
public class arrays {

    public static String compress(String str){
        StringBuilder ret = new StringBuilder();
        int curr_count = 1;
        char curr_char = str.charAt(0);
        for(int i = 1; i < str.length(); i++){
            if(str.charAt(i) != curr_char){
                ret.append(curr_char);
                ret.append(curr_count);
                curr_count = 1;
                curr_char = str.charAt(i);
            }
            else{
                curr_count +=1;
            }
        }
        ret.append(curr_char);
        ret.append(curr_count);
        if(ret.toString().length() < str.length()){
            return ret.toString();
        }
        else{
            return str;
        }
    }

    public static void main(String[] args) {
        String test1 = "ab";
        String test2 = "aa";
        String test3 = "aabcccccaaa";
        System.out.println(compress(test3));
    }
}
