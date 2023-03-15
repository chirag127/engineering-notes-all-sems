## 28.WAP to implement strlen (), strcat (),strcpy () using the concept of Functions.

- The strlen () function returns the length of a given string, excluding the null character at the end.
- The strcat () function appends one string to the end of another string, and returns the concatenated string.
- The strcpy () function copies one string to another string, and returns the destination string.
- These functions can be implemented using the concept of functions in C programming language, as shown below:

```c
// A function to return the length of a string
int strlen (char *str)
{
    int len = 0; // a variable to store the length
    while (*str != '\0') // loop until the end of the string
    {
        len++; // increment the length
        str++; // move the pointer to the next character
    }
    return len; // return the length
}

// A function to append one string to another string
char *strcat (char *dest, char *src)
{
    char *temp = dest; // a pointer to store the original destination string
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
    return temp; // return the original destination string
}

// A function to copy one string to another string
char *strcpy (char *dest, char *src)
{
    char *temp = dest; // a pointer to store the original destination string
    while (*src != '\0') // loop until the end of the source string
    {
        *dest = *src; // copy the character from the source to the destination
        dest++; // move the pointer to the next character
        src++; // move the pointer to the next character
    }
    *dest = '\0'; // add a null character at the end of the destination string
    return temp; // return the original destination string
}
```