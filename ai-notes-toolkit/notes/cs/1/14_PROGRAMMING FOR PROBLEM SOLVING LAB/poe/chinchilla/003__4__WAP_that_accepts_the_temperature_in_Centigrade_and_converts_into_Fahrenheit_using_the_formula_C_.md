## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

When working with temperature units, it is important to be able to convert between different units. One common conversion is between the Celsius and Fahrenheit scales. In this topic, we will learn how to write a program that converts a temperature in Centigrade (Celsius) to Fahrenheit using the formula C/5=(F-32)/9.

Here are the steps to write a program that accepts the temperature in Centigrade and converts it into Fahrenheit:

1. Start by creating a new program in your preferred programming language.

2. Define a variable to hold the temperature in Centigrade. You can name this variable whatever you like, but we will use the name "celsius" for this example.

3. Prompt the user to enter the temperature in Centigrade. You can use the input() function in Python or the Scanner class in Java to get user input.

4. Convert the temperature from Centigrade to Fahrenheit using the formula C/5=(F-32)/9. Here's how you can do it in code:

   ```
   fahrenheit = (celsius * 9/5) + 32
   ```

   This formula takes the temperature in Centigrade and multiplies it by 9/5 (or 1.8) to get the temperature in Fahrenheit. Then, it adds 32 to the result to get the final temperature in Fahrenheit.

5. Print out the temperature in Fahrenheit to the user. You can use the print() function in Python or the System.out.println() method in Java to display the result.

   ```
   print("The temperature in Fahrenheit is:", fahrenheit)
   ```

   This will display the temperature in Fahrenheit to the user.

6. Test your program with different input values to make sure it works correctly.

That's it! With these steps, you can write a program that accepts the temperature in Centigrade and converts it into Fahrenheit using the formula C/5=(F-32)/9.