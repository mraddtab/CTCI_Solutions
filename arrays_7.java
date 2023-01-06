import java.util.Arrays;
import java.lang.Math;
import java.util.HashMap;
public class arrays {

    static void printMatrix(int[][] mat){
        for(int i = 0; i <mat.length; i ++) {
            for (int j = 0; j < mat[i].length; j++) {
                System.out.print(mat[i][j]);
            }
            System.out.println();
        }
    }

    static int[][] rotateMatrix(int[][] matrix){
        for(int layer = 0; layer < matrix.length/2; layer++){
            int first = layer;
            int last = matrix.length - 1 - layer;
            for(int i = first; i < last; i++){
                int offset = i - first;
                int top = matrix[first][i];         //Save top
                //left -> top
                matrix[first][i] = matrix[last - offset][first];
                //bottom -> left
                matrix[last-offset][first] = matrix[last][last - offset];
                //right -> bottom
                matrix[last][last - offset] = matrix[i][last];
                //top -> right
                matrix[i][last] = top;
            }
        }
        return matrix;
    }
    public static void main(String[] args) {
        int matrix2[][] = {{1,2},{3,4}};
        int matrix3[][] = { {1,2,3},{4,5,6},{7,8,9}};
        int matrix4[][] = { {1,2,3,4},{5,6,7,8}, {9,10,11,12}, {13,14,15,16}};
        printMatrix(rotateMatrix(matrix3));
    }

}
