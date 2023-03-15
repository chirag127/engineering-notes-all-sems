## 28.WAP to implement strlen (), strcat (),strcpy () using the concept of Functions.

- The strlen() function returns the length of a given string. It does not count the null character '\0' at the end of the string.
- The strcat() function appends one string to the end of another string. It assumes that the destination string has enough space to hold the concatenated result. It also overwrites the null character of the destination string with the first character of the source string, and adds a null character at the end of the concatenated string.
- The strcpy() function copies one string to another string. It assumes that the destination string has enough space to hold the source string. It also copies the null character from the source string to the destination string.

- Here is a possible C program to implement these functions using the concept of functions:

```c
#include <stdio.h>

// A function to return the length of a string
int strlen(char *s)
{
    int len = 0; // Initialize a variable to store the length
    while (*s != '\0') // Loop until the end of the string
    {
        len++; // Increment the length
        s++; // Move the pointer to the next character
    }
    return len; // Return the length
}

// A function to append one string to another string
void strcat(char *dest, char *src)
{
    while (*dest != '\0') // Loop until the end of the destination string
    {
        dest++; // Move the pointer to the next character
    }
    while (*src != '\0') // Loop until the end of the source string
    {
        *dest = *src; // Copy the character from the source to the destination
        dest++; // Move the pointer to the next character
        src++; // Move the pointer to the next character
    }
    *dest = '\0'; // Add a null character at the end of the concatenated string
}

// A function to copy one string to another string
void strcpy(char *dest, char *src)
{
    while (*src != '\0') // Loop until the end of the source string
    {
        *dest = *src; // Copy the character from the source to the destination
        dest++; // Move the pointer to the next character
        src++; // Move the pointer to the next character
    }
    *dest = '\0'; // Add a null character at the end of the copied string
}

// A main function to test the above functions
int main()
{
    char s1[20] = "Hello"; // Declare and initialize a string
    char s2[20] = "World"; // Declare and initialize another string
    char s3[20]; // Declare a string to hold the result

    printf("The length of s1 is %d\n", strlen(s1)); // Print the length of s1
    printf("The length of s2 is %d\n", strlen(s2)); // Print the length of s2

    strcpy(s3, s1); // Copy s1 to s3
    printf("The string s3 is %s\n", s3); // Print s3

    strcat(s3, s2); // Append s2 to s3
    printf("The string s3 is %s\n", s3); // Print s3

    return 0; // Return 0 to indicate successful termination
}
```