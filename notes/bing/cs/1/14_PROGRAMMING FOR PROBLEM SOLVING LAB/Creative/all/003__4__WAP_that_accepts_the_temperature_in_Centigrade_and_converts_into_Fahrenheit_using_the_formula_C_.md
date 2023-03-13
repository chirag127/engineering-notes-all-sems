## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

- WAP stands for Write a Program, which is a common abbreviation used in programming assignments and exercises.
- The problem statement is to write a program that accepts the temperature in Centigrade (also known as Celsius) and converts it into Fahrenheit using the given formula.
- The formula is derived from the fact that the freezing point of water is 0°C in Centigrade and 32°F in Fahrenheit, and the boiling point of water is 100°C in Centigrade and 212°F in Fahrenheit. Therefore, the difference between the two scales is 100°C = 180°F, or 1°C = 1.8°F.
- To solve this problem, we need to follow these steps:
  - Declare a variable to store the temperature in Centigrade, and assign it a value from the user input.
  - Declare another variable to store the temperature in Fahrenheit, and assign it the value obtained by applying the formula to the first variable.
  - Print the result to the output.
- Here is an example of how the program can be written in Python, which is a popular programming language:

```python
# WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

# Declare a variable to store the temperature in Centigrade, and assign it a value from the user input.
C = float(input("Enter the temperature in Centigrade: "))

# Declare another variable to store the temperature in Fahrenheit, and assign it the value obtained by applying the formula to the first variable.
F = (C * 9 / 5) + 32

# Print the result to the output.
print("The temperature in Fahrenheit is: ", F)
```

- Here is an example of how the program can be written in C, which is another popular programming language:

```c
// WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

#include <stdio.h>

int main()
{
    // Declare a variable to store the temperature in Centigrade, and assign it a value from the user input.
    float C;
    printf("Enter the temperature in Centigrade: ");
    scanf("%f", &C);

    // Declare another variable to store the temperature in Fahrenheit, and assign it the value obtained by applying the formula to the first variable.
    float F;
    F = (C * 9 / 5) + 32;

    // Print the result to the output.
    printf("The temperature in Fahrenheit is: %f\n", F);

    return 0;
}
```

- Here are some possible mnemonics and learning tricks for the formula C/5=(F-32)/9:
  - Remember that C stands for Centigrade and F stands for Fahrenheit, and they are both divided by 5 and 9 respectively.
  - Remember that F has 32 added to it, which is the difference between the freezing points of the two scales.
  - Remember that 9 is larger than 5, which means that Fahrenheit is larger than Centigrade for the same temperature.
  - Remember that the formula can be rearranged to get F = (C * 9 / 5) + 32 or C = (F - 32) * 5 / 9, depending on which conversion you need to do.