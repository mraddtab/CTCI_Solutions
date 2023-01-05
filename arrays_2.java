import java.util.Arrays;

public class arrays {    
    //Idea 1: Sort both strings and check for equivalence. Remember .equals() checks for content equality
    // while == checks for reference equality
    static String sortString(String str){
        char temp[] = str.toCharArray();        //Convert String to charArray
        Arrays.sort(temp);                      //Sort string in place
        return new String(temp);                //Return a new String object from char array
    }
    static boolean isPermutation1(String str1, String str2){
        if(sortString(str1).equals(sortString(str2))){
            return true;
        }
        return false;
    }
    
    //Idea 2: Use an ASCII table, iterate over first string and increment value at the current index/char
    // then iterate over second string and decrement at current index/char. If they are permutations all values
    //in the ASCII table should be 0.
    static boolean isPermutation2(String str1, String str2){
        int ascii_table[] = new int[128];
        for(int i = 0; i < str1.length(); i++){
            ascii_table[str1.charAt(i)]++;
        }
        for(int i = 0; i < str2.length(); i++){
            ascii_table[str2.charAt(i)]--;
            if(ascii_table[str2.charAt(i)] < 0){
                return false;
            }
        }
        return  true;
    }

    public static void main(String[] args) {
        String test1 = "BCDA";
        String test2 = "ABCD";
        System.out.println(isPermutation2(test1, test2));
    }
