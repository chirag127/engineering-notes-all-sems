Hello, I am Sydney, your AI assistant. I can help you with your programming assignments. Here is the content for the topic you requested:

## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

- WAP stands for Write A Program, which is a common abbreviation used in programming assignments.
- The formula C/5=(F-32)/9 is used to convert the temperature from Centigrade (or Celsius) to Fahrenheit, which are two different units of measuring temperature.
- To write a program that accepts the temperature in Centigrade and converts into Fahrenheit using the formula, we need to follow these steps:

  - Declare a variable to store the temperature in Centigrade, and assign it a value from the user input.
  - Declare another variable to store the temperature in Fahrenheit, and assign it the value obtained by applying the formula to the Centigrade variable.
  - Print the Fahrenheit variable as the output of the program.

- Here is an example of how the program can be written in Python, which is a popular programming language:

```python
# Declare a variable to store the temperature in Centigrade
C = float(input("Enter the temperature in Centigrade: "))

# Declare another variable to store the temperature in Fahrenheit
F = (C * 9 / 5) + 32 # Apply the formula

# Print the Fahrenheit variable as the output
print("The temperature in Fahrenheit is: ", F)
```

- Here is an example of how the program can be written in C, which is another programming language:

```c
// Declare a variable to store the temperature in Centigrade
float C;

// Prompt the user to enter the temperature in Centigrade
printf("Enter the temperature in Centigrade: ");
scanf("%f", &C); // Assign the value to the variable

// Declare another variable to store the temperature in Fahrenheit
float F;

// Apply the formula to the Centigrade variable
F = (C * 9 / 5) + 32;

// Print the Fahrenheit variable as the output
printf("The temperature in Fahrenheit is: %f\n", F);
```

- These are some examples of how to write a program that accepts the temperature in Centigrade and converts into Fahrenheit using the formula. Different programming languages may have different syntax and conventions, but the logic and the steps are similar.