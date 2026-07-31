Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program that simply takes elements of the array from the user and finds the sum of these elements. Here is the content in markdown format:

# 21. WAP that simply takes elements of the array from the user and finds the sum of these elements.

- An array is a collection of data items of the same type, stored in contiguous memory locations.
- To take elements of the array from the user, we need to use a loop and a scanner object to read the input from the keyboard.
- To find the sum of these elements, we need to use another loop and a variable to store the running total.
- Here is an example of such a program in Java:

```java
import java.util.Scanner; // import the scanner class

public class ArraySum {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in); // create a scanner object
    System.out.println("Enter the size of the array: "); // prompt the user for the size of the array
    int n = sc.nextInt(); // read the size from the user
    int[] arr = new int[n]; // create an array of size n
    System.out.println("Enter the elements of the array: "); // prompt the user for the elements of the array
    for (int i = 0; i < n; i++) { // loop through the array
      arr[i] = sc.nextInt(); // read each element from the user and store it in the array
    }
    int sum = 0; // initialize a variable to store the sum
    for (int num : arr) { // loop through the array using the enhanced for loop
      sum += num; // add each element to the sum
    }
    System.out.println("The sum of the elements of the array is: " + sum); // print the sum
    sc.close(); // close the scanner
  }
}
```