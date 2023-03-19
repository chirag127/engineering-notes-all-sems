## 1. WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student.

In this program, we will create a Python script that accepts the marks of 5 subjects and calculates the sum and percentage of marks obtained by the student. Here are the steps to write this program:

1. Start by declaring 5 variables to store the marks obtained in each subject. We will use the input() function to get the marks from the user. The syntax for input() function is:

   ```
   variable_name = input("Enter the marks obtained in subject: ")
   ```

2. After getting the marks, we need to convert them to integers using the int() function. The syntax for int() function is:

   ```
   variable_name = int(variable_name)
   ```

3. Now, we can calculate the sum of marks by adding the values of all 5 variables. The syntax for addition is:

   ```
   sum = variable1 + variable2 + variable3 + variable4 + variable5
   ```

4. To calculate the percentage of marks, we need to divide the sum of marks by the total marks and multiply by 100. The total marks in this case is 500 (assuming each subject has a maximum of 100 marks). The syntax for percentage calculation is:

   ```
   percentage = (sum/500) * 100
   ```

5. Finally, we can print the sum and percentage of marks obtained by the student using the print() function. The syntax for print() function is:

   ```
   print("Sum of marks: ", sum)
   print("Percentage of marks: ", percentage)
   ```

Here is the complete Python code to implement this program:

```
# Accept the marks of 5 subjects
subject1 = int(input("Enter the marks obtained in subject 1: "))
subject2 = int(input("Enter the marks obtained in subject 2: "))
subject3 = int(input("Enter the marks obtained in subject 3: "))
subject4 = int(input("Enter the marks obtained in subject 4: "))
subject5 = int(input("Enter the marks obtained in subject 5: "))

# Calculate the sum of marks
sum = subject1 + subject2 + subject3 + subject4 + subject5

# Calculate the percentage of marks
percentage = (sum/500) * 100

# Print the sum and percentage of marks
print("Sum of marks: ", sum)
print("Percentage of marks: ", percentage)
```

By running this program, you will be able to accept the marks of 5 subjects and find the sum and percentage of marks obtained by the student.