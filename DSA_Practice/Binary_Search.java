import java.util.Scanner;

public class Binary_Search {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of an array:");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the elements of an array:");
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        System.out.println("Enter the target element:");
        int target = sc.nextInt();
        int start = 0;
        int end = n - 1;    
        while(start <= end){
            int mid = start + (end - start) / 2;
            if(arr[mid] == target){
                System.out.println("Element found at index: " + mid);
                return;
            }   
            else if(arr[mid] < target){
                start = mid + 1;
            }
            else{
                end = mid - 1;
            }           
        }
        System.out.println("Element not found");

        sc.close();
    }
}