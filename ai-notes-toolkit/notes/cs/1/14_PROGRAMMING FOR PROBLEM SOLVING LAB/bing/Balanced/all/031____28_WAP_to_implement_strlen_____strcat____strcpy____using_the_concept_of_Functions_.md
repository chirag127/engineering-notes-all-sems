## 28.WAP to implement strlen (), strcat (),strcpy () using the concept of Functions.

- The strlen() function returns the length of a given string, excluding the null character at the end.
- The strcat() function appends a copy of one string to the end of another string, and returns a pointer to the resulting string.
- The strcpy() function copies one string to another string, and returns a pointer to the destination string.
- These functions can be implemented using the concept of functions in C programming language, as shown below:

```c
// A function to return the length of a string
int strlen(char *str)
{
    int len = 0; // a variable to store the length
    while (*str != '\0') // loop until the end of the string
    {
        len++; // increment the length
        str++; // move the pointer to the next character
    }
    return len; // return the length
}

// A function to append one string to another
char *strcat(char *dest, char *src)
{
    char *temp = dest; // a pointer to store the original destination
    while (*dest != '\0') // loop until the end of the destination string
    {
        dest++; // move the pointer to the next character
    }
    while (*src != '\0') // loop until the end of the source string
    {
        *dest = *src; // copy the character from the source to the destination
        dest++; // move the pointer to the next character
        src++; // move the pointer to the next character
    }
    *dest = '\0'; // add a null character at the end of the destination string
    return temp; // return the original destination pointer
}

// A function to copy one string to another
char *strcpy(char *dest, char *src)
{
    char *temp = dest; // a pointer to store the original destination
    while (*src != '\0') // loop until the end of the source string
    {
        *dest = *src; // copy the character from the source to the destination
        dest++; // move the pointer to the next character
        src++; // move the pointer to the next character
    }
    *dest = '\0'; // add a null character at the end of the destination string
    return temp; // return the original destination pointer
}
```