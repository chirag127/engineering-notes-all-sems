Hello, I am Sydney, your AI assistant. I can help you with your programming tasks. Here is the content you requested:

## 28.WAP to implement strlen (), strcat (),strcpy () using the concept of Functions.

- In this program, we will implement three string functions: strlen (), strcat (), and strcpy () using the concept of functions in C language.
- A function is a block of code that performs a specific task and can be reused in different parts of the program.
- A string is a sequence of characters terminated by a null character ('\0').
- The strlen () function returns the length of a string, excluding the null character.
- The strcat () function appends one string to the end of another string, and returns the concatenated string.
- The strcpy () function copies one string to another string, and returns the destination string.

- Here is the code for the program:

```c
#include <stdio.h>

// Function to return the length of a string
int strlen (char *str)
{
    int len = 0; // Variable to store the length
    while (*str != '\0') // Loop until the null character is reached
    {
        len++; // Increment the length
        str++; // Move the pointer to the next character
    }
    return len; // Return the length
}

// Function to append one string to the end of another string
char *strcat (char *dest, char *src)
{
    char *temp = dest; // Store the original destination pointer
    while (*dest != '\0') // Loop until the end of the destination string is reached
    {
        dest++; // Move the pointer to the next character
    }
    while (*src != '\0') // Loop until the end of the source string is reached
    {
        *dest = *src; // Copy the character from the source to the destination
        dest++; // Move the destination pointer to the next character
        src++; // Move the source pointer to the next character
    }
    *dest = '\0'; // Add the null character at the end of the destination string
    return temp; // Return the original destination pointer
}

// Function to copy one string to another string
char *strcpy (char *dest, char *src)
{
    char *temp = dest; // Store the original destination pointer
    while (*src != '\0') // Loop until the end of the source string is reached
    {
        *dest = *src; // Copy the character from the source to the destination
        dest++; // Move the destination pointer to the next character
        src++; // Move the source pointer to the next character
    }
    *dest = '\0'; // Add the null character at the end of the destination string
    return temp; // Return the original destination pointer
}

// Main function to test the functions
int main ()
{
    char str1[20] = "Hello"; // Declare and initialize a string
    char str2[20] = "World"; // Declare and initialize another string
    char str3[20]; // Declare a string to store the result of strcpy ()
    printf ("The length of str1 is %d\n", strlen (str1)); // Print the length of str1
    printf ("The length of str2 is %d\n", strlen (str2)); // Print the length of str2
    printf ("The concatenation of str1 and str2 is %s\n", strcat (str1, str2)); // Print the concatenation of str1 and str2
    printf ("The copy of str2 to str3 is %s\n", strcpy (str3, str2)); // Print the copy of str2 to str3
    return 0; // Return 0 to indicate successful termination
}
```

- Here is the output of the program:

```text
The length of str1 is 5
The length of str2 is 5
The concatenation of str1 and str2 is HelloWorld
The copy of str2 to str3 is World
```