import java.util.Scanner;

public class Fibonacci_Search {
    public static int fibonaccianSearch(int[] arr, int x, int n) {
        int fibM2 = 0, fibM1 = 1, fibM = fibM2 + fibM1;

        while (fibM < n) {
            fibM2 = fibM1;
            fibM1 = fibM;
            fibM = fibM2 + fibM1;
        }

        int offset = -1;

        while (fibM > 1) {
            int i = Math.min(offset + fibM2, n - 1);

            if (arr[i] < x) {
                fibM = fibM1;
                fibM1 = fibM2;
                fibM2 = fibM - fibM1;
                offset = i;
            } else if (arr[i] > x) {
                fibM = fibM2;
                fibM1 = fibM1 - fibM2;
                fibM2 = fibM - fibM1;
            } else {
                return i;
            }
        }

        if (fibM1 == 1 && arr[offset + 1] == x) return offset + 1;

        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();
        int[] arr = new int[n];

        System.out.println("Enter " + n + " sorted elements:");
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        System.out.print("Enter element to search: ");
        int x = sc.nextInt();

        int result = fibonaccianSearch(arr, x, n);

        if (result >= 0) System.out.println("Element found at index: " + result);
        else System.out.println("Element not found");

        sc.close();
    }
}
