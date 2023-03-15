Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program to find the greatest of three numbers. Here is the content in markdown format:

## 7. WAP to find the greatest of three numbers.

- To find the greatest of three numbers, we need to compare them using some conditional statements, such as `if`, `else if`, and `else`.
- We can use the `>` operator to check if one number is greater than another, and the `==` operator to check if two numbers are equal.
- We can use the `Scanner` class to take input from the user, and the `System.out.println()` method to print the output.
- Here is the algorithm for the program:

```
1. Create a Scanner object to take input from the user.
2. Declare three int variables, a, b, and c, and assign them the values entered by the user.
3. Declare another int variable, max, to store the greatest number.
4. If a is greater than b and a is greater than c, then assign a to max.
5. Else if b is greater than a and b is greater than c, then assign b to max.
6. Else if c is greater than a and c is greater than b, then assign c to max.
7. Else, all the numbers are equal, and assign any of them to max.
8. Print the value of max as the greatest number.
9. Close the Scanner object.
```

- Here is the code for the program in Java:

```java
// import the Scanner class
import java.util.Scanner;

// create a class named GreatestOfThree
public class GreatestOfThree {

  // create the main method
  public static void main(String[] args) {

    // create a Scanner object to take input from the user
    Scanner sc = new Scanner(System.in);

    // declare three int variables, a, b, and c, and assign them the values entered by the user
    System.out.println("Enter three numbers:");
    int a = sc.nextInt();
    int b = sc.nextInt();
    int c = sc.nextInt();

    // declare another int variable, max, to store the greatest number
    int max;

    // if a is greater than b and a is greater than c, then assign a to max
    if (a > b && a > c) {
      max = a;
    }
    // else if b is greater than a and b is greater than c, then assign b to max
    else if (b > a && b > c) {
      max = b;
    }
    // else if c is greater than a and c is greater than b, then assign c to max
    else if (c > a && c > b) {
      max = c;
    }
    // else, all the numbers are equal, and assign any of them to max
    else {
      max = a;
    }

    // print the value of max as the greatest number
    System.out.println("The greatest number is " + max);

    // close the Scanner object
    sc.close();
  }
}
```

- Here is a sample input and output for the program:

```
Enter three numbers:
10
20
15
The greatest number is 20
```