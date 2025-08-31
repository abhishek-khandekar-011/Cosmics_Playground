import java.util.Scanner;

public class Linear_Search {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input array size
        System.out.println("Enter the size of the array: ");
        int n = sc.nextInt();

        // Declare array
        int[] arr = new int[n];

        // Input elements
        System.out.println("Enter the elements of the array: ");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // Input target element
        System.out.println("Enter the target element: ");
        int target = sc.nextInt();

        // Linear search logic
        for (int i = 0; i < n; i++) {
            if (arr[i] == target) {
                System.out.println("Element found at index: " + i);
                sc.close();
                return; // exit after finding
            }
        }

        // If not found
        System.out.println("Element not found");
        sc.close();
    }
}
