## Between 90-100%-----Print ‘A’

- This is a common programming task that involves using conditional statements to check the value of a variable or expression and print a corresponding letter grade.
- A possible pseudocode for this task is:

```
if score is between 90 and 100 inclusive
    print "A"
else
    print "Not A"
```

- A possible Python code for this task is:

```python
score = int(input("Enter your score: ")) # get the score from the user
if score >= 90 and score <= 100: # check if the score is between 90 and 100
    print("A") # print A
else:
    print("Not A") # print Not A
```

- A possible C code for this task is:

```c
#include <stdio.h>
int main()
{
    int score; // declare a variable to store the score
    printf("Enter your score: "); // prompt the user to enter the score
    scanf("%d", &score); // read the score from the user
    if (score >= 90 && score <= 100) // check if the score is between 90 and 100
    {
        printf("A\n"); // print A
    }
    else
    {
        printf("Not A\n"); // print Not A
    }
    return 0;
}
```

- A possible Java code for this task is:

```java
import java.util.Scanner;
public class Grade {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // create a scanner object to get the user input
        System.out.println("Enter your score: "); // prompt the user to enter the score
        int score = sc.nextInt(); // read the score from the user
        if (score >= 90 && score <= 100) // check if the score is between 90 and 100
        {
            System.out.println("A"); // print A
        }
        else
        {
            System.out.println("Not A"); // print Not A
        }
        sc.close(); // close the scanner object
    }
}
```

- A possible C# code for this task is:

```csharp
using System;
class Grade {
    static void Main() {
        Console.WriteLine("Enter your score: "); // prompt the user to enter the score
        int score = int.Parse(Console.ReadLine()); // read the score from the user
        if (score >= 90 && score <= 100) // check if the score is between 90 and 100
        {
            Console.WriteLine("A"); // print A
        }
        else
        {
            Console.WriteLine("Not A"); // print Not A
        }
    }
}
```