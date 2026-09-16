import java.util.Scanner;
public class Half_Pyramid {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter the number of rows:");

        int rows = sc.nextInt();

        for(int i = 0; i < rows + 1 ; i++){

            for(int j = 0; j < i; j++){
                
                System.out.print("* ");
            }
       
            System.out.println();

        }

        sc.close();
