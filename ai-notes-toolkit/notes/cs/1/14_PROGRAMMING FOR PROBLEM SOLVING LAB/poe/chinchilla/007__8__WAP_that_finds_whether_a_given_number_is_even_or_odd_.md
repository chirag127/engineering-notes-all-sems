## 8. WAP that finds whether a given number is even or odd.

When writing computer programs, one common task is to determine whether a given number is even or odd. This is particularly important when dealing with numbers that are input by users, as it allows us to perform different operations depending on whether the number is even or odd. Here are some points to keep in mind when writing a computer program to determine whether a number is even or odd:

1. An even number is any number that can be divided by 2 without leaving a remainder. For example, 2, 4, 6, 8, and 10 are all even numbers.

2. An odd number is any number that cannot be divided by 2 without leaving a remainder. For example, 1, 3, 5, 7, and 9 are all odd numbers.

3. One way to determine whether a number is even or odd is to use the modulus operator (%). The modulus operator returns the remainder when one number is divided by another. For example, 5 % 2 returns 1, because 5 divided by 2 leaves a remainder of 1. By checking the remainder when dividing a number by 2, we can determine whether the number is even or odd. If the remainder is 0, the number is even. If the remainder is 1, the number is odd.

4. Here is an example program that uses the modulus operator to determine whether a number is even or odd:

```
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
```

5. In this program, we first prompt the user to enter a number using the input() function. We then convert the user's input to an integer using the int() function. We store the input number in a variable called num.

6. We then use an if/else statement to check whether the number is even or odd. We do this by checking the remainder when the number is divided by 2 using the modulus operator. If the remainder is 0, we print a message saying that the number is even. If the remainder is 1, we print a message saying that the number is odd.

7. It is important to note that the modulus operator only works with integers. If you need to determine whether a non-integer number is even or odd, you will need to use a different approach.

8. In summary, determining whether a number is even or odd is a common task in programming. By using the modulus operator, we can easily check whether a number is even or odd and perform different operations depending on the result.