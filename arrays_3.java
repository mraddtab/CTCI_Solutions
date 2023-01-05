import java.util.Arrays;

public class arrays {

    public static int countChar(String str, char c, int trueLen){
        int ret = 0;
        for(int i = 0; i < trueLen; i++){
            if(str.charAt(i) == c){
                ret +=1;
            }
        }
        return ret;
    }
    public static String urlify(String str, int trueLen){
        char ret[] = str.toCharArray();
        int spaces = countChar(str, ' ', trueLen) * 2;
        for(int i = trueLen-1; i >= 0; i--){
            if(ret[i] != ' '){
                ret[i + spaces] = ret[i];
            }
            else{
                ret[i + spaces - 2] = '%';
                ret[i + spaces - 1] = '2';
                ret[i + spaces] = '0';
                spaces -= 2;
            }
        }
        return new String(ret);
    }

    public static void main(String[] args) {
        System.out.println(urlify("mr  john smith      ", 14));
    }
}
