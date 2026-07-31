Hello, I am Sydney, your AI assistant. I can help you with your programming tasks. Here is the content you requested:

## 28.WAP to implement strlen (), strcat (),strcpy () using the concept of Functions.

- In this program, we will implement three string functions: strlen (), strcat (), and strcpy () using the concept of functions in C language.
- The strlen () function returns the length of a string, excluding the null terminator '\0'.
- The strcat () function appends a copy of the source string to the end of the destination string, and returns the destination string.
- The strcpy () function copies the source string to the destination string, and returns the destination string.
- We will define our own functions to perform these operations, and use them in the main function to test them.

```c
#include <stdio.h>

// Function to return the length of a string
int my_strlen(char *s)
{
    int len = 0; // Initialize length variable
    while (*s != '\0') // Loop until null terminator is found
    {
        len++; // Increment length
        s++; // Move pointer to next character
    }
    return len; // Return length
}

// Function to append a source string to a destination string
char *my_strcat(char *dest, char *src)
{
    char *temp = dest; // Store the original destination pointer
    while (*dest != '\0') // Loop until the end of destination string is reached
    {
        dest++; // Move pointer to next character
    }
    while (*src != '\0') // Loop until the end of source string is reached
    {
        *dest = *src; // Copy character from source to destination
        dest++; // Move destination pointer to next character
        src++; // Move source pointer to next character
    }
    *dest = '\0'; // Add null terminator to the end of destination string
    return temp; // Return the original destination pointer
}

// Function to copy a source string to a destination string
char *my_strcpy(char *dest, char *src)
{
    char *temp = dest; // Store the original destination pointer
    while (*src != '\0') // Loop until the end of source string is reached
    {
        *dest = *src; // Copy character from source to destination
        dest++; // Move destination pointer to next character
        src++; // Move source pointer to next character
    }
    *dest = '\0'; // Add null terminator to the end of destination string
    return temp; // Return the original destination pointer
}

// Main function to test the functions
int main()
{
    char s1[20] = "Hello"; // Declare and initialize a string
    char s2[20] = "World"; // Declare and initialize another string
    char s3[20]; // Declare an empty string

    printf("The length of s1 is %d\n", my_strlen(s1)); // Print the length of s1 using my_strlen function
    printf("The length of s2 is %d\n", my_strlen(s2)); // Print the length of s2 using my_strlen function

    my_strcat(s1, s2); // Append s2 to s1 using my_strcat function
    printf("The concatenated string is %s\n", s1); // Print the concatenated string

    my_strcpy(s3, s1); // Copy s1 to s3 using my_strcpy function
    printf("The copied string is %s\n", s3); // Print the copied string

    return 0; // Return 0 to indicate successful execution
}
```