import java.util.Arrays;
import java.lang.Math;
import java.util.HashMap;
public class arrays {

    public static boolean sameLength(String str1, String str2){
        int diffs = 0;
        String shorterStr = (str1.length() <= str2.length()) ? str1 : str2;
        for(int i = 0; i < shorterStr.length(); i++){
            if(str1.charAt(i) != str2.charAt(i)){
                diffs +=1;
            }
        }
        return diffs <= 1;
    }
    public static boolean oneAway(String str1, String str2){
        if (Math.abs(str1.length() - str2.length()) > 1){
            return false;
        }
        if (str1.length() == str2.length()){
            return sameLength(str1, str2);
        }
        String shorterStr = (str1.length() <= str2.length()) ? str1 : str2;
        String longestStr = (str1.length() < str2.length()) ? str2 : str1;
        int diffs = 0;
        int shorterPtr = 0;
        int longerPtr = 0;
        while(shorterPtr < shorterStr.length()){
            if(shorterStr.charAt(shorterPtr) != longestStr.charAt(longerPtr)){
                longerPtr+=1;
                diffs +=1;
            }
            else{
                longerPtr+=1;
                shorterPtr+=1;
            }
        }
        if(diffs > 1){
            return false;
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(oneAway("pale", "ple"));
        System.out.println(oneAway("pales", "pale"));
        System.out.println(oneAway("pale", "bale"));
        System.out.println(oneAway("pale", "bake"));

    }
}
