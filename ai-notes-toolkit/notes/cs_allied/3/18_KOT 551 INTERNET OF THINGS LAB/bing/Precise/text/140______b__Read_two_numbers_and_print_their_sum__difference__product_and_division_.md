#### b) Read two numbers and print their sum, difference, product and division.

To solve this problem, we need to follow these steps:

1. Read two numbers from the user. This can be done using the `input()` function in Python, or by using `Scanner` class in Java.
2. Calculate the sum of the two numbers by adding them together.
3. Calculate the difference of the two numbers by subtracting one from the other.
4. Calculate the product of the two numbers by multiplying them together.
5. Calculate the division of the two numbers by dividing one by the other.
6. Print the results of the sum, difference, product, and division.

Here is an example of how this can be done in Python:

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)
```

And here is an example of how this can be done in Java:

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the first number: ");
        int num1 = scanner.nextInt();
        System.out.print("Enter the second number: ");
        int num2 = scanner.nextInt();

        int sum = num1 + num2;
        int difference = num1 - num2;
        int product = num1 * num2;
        double division = (double) num1 / num2;

        System.out.println("Sum: " + sum);
        System.out.println("Difference: " + difference);
        System.out.println("Product: " + product);
        System.out.println("Division: " + division);
    }
}
```