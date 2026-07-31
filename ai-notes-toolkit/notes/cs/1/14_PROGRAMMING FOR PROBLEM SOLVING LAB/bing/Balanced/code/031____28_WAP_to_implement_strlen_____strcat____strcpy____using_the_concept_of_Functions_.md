Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write a program to implement strlen(), strcat(), and strcpy() using the concept of functions. Here is the content in markdown format:

## 28.WAP to implement strlen(), strcat(), strcpy() using the concept of functions.

- The strlen() function returns the length of a string, excluding the null character at the end.
- The strcat() function appends one string to the end of another string, and returns the concatenated string.
- The strcpy() function copies one string to another string, and returns the destination string.
- To implement these functions using the concept of functions, we need to define our own functions that take string parameters and perform the required operations using loops and pointers.
- Here is an example of how to implement these functions in C language:

```c
#include <stdio.h>

// A function to return the length of a string
int my_strlen(char *str)
{
    int len = 0; // Initialize a variable to store the length
    while (*str != '\0') // Loop until the end of the string
    {
        len++; // Increment the length
        str++; // Move the pointer to the next character
    }
    return len; // Return the length
}

// A function to append one string to the end of another string
char *my_strcat(char *dest, char *src)
{
    char *temp = dest; // Store the original destination pointer
    while (*dest != '\0') // Loop until the end of the destination string
    {
        dest++; // Move the pointer to the next character
    }
    while (*src != '\0') // Loop until the end of the source string
    {
        *dest = *src; // Copy the character from the source to the destination
        dest++; // Move the destination pointer to the next character
        src++; // Move the source pointer to the next character
    }
    *dest = '\0'; // Add a null character at the end of the destination string
    return temp; // Return the original destination pointer
}

// A function to copy one string to another string
char *my_strcpy(char *dest, char *src)
{
    char *temp = dest; // Store the original destination pointer
    while (*src != '\0') // Loop until the end of the source string
    {
        *dest = *src; // Copy the character from the source to the destination
        dest++; // Move the destination pointer to the next character
        src++; // Move the source pointer to the next character
    }
    *dest = '\0'; // Add a null character at the end of the destination string
    return temp; // Return the original destination pointer
}

// A main function to test the above functions
int main()
{
    char str1[20] = "Hello"; // Declare and initialize a string
    char str2[20] = "World"; // Declare and initialize another string
    printf("The length of str1 is %d\n", my_strlen(str1)); // Print the length of str1 using my_strlen()
    printf("The length of str2 is %d\n", my_strlen(str2)); // Print the length of str2 using my_strlen()
    printf("The concatenation of str1 and str2 is %s\n", my_strcat(str1, str2)); // Print the concatenation of str1 and str2 using my_strcat()
    printf("The copy of str2 to str1 is %s\n", my_strcpy(str1, str2)); // Print the copy of str2 to str1 using my_strcpy()
    return 0; // Return 0 to indicate successful execution
}
```