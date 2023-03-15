Hello, I am Sydney, your AI assistant. I can help you with your programming tasks. Here is the content you requested:

## 28.WAP to implement strlen (), strcat (),strcpy () using the concept of Functions.

- The strlen () function returns the length of a string, excluding the null terminator.
- The strcat () function appends a copy of one string to the end of another string, and adds a null terminator.
- The strcpy () function copies one string to another string, and adds a null terminator.
- These functions can be implemented using the concept of functions in C programming language.
- A function is a block of code that performs a specific task and can be reused in a program.
- A function has a name, a list of parameters, a return type, and a body.
- A function can be defined before or after the main () function, or in a separate source file.
- A function can be called by using its name and passing the required arguments.
- Here is an example of how to implement strlen (), strcat (), and strcpy () using the concept of functions:

```c
// A function to return the length of a string
int strlen (char *str)
{
    int len = 0; // a variable to store the length
    while (*str != '\0') // loop until the end of the string
    {
        len++; // increment the length
        str++; // move to the next character
    }
    return len; // return the length
}

// A function to append a string to another string
void strcat (char *dest, char *src)
{
    while (*dest != '\0') // loop until the end of the destination string
    {
        dest++; // move to the next character
    }
    while (*src != '\0') // loop until the end of the source string
    {
        *dest = *src; // copy the character
        dest++; // move to the next character
        src++; // move to the next character
    }
    *dest = '\0'; // add a null terminator
}

// A function to copy a string to another string
void strcpy (char *dest, char *src)
{
    while (*src != '\0') // loop until the end of the source string
    {
        *dest = *src; // copy the character
        dest++; // move to the next character
        src++; // move to the next character
    }
    *dest = '\0'; // add a null terminator
}

// A main function to test the functions
int main ()
{
    char str1[20] = "Hello"; // a string to store "Hello"
    char str2[20] = "World"; // a string to store "World"
    char str3[20]; // a string to store the copy of str1
    printf ("The length of str1 is %d\n", strlen (str1)); // print the length of str1
    printf ("The length of str2 is %d\n", strlen (str2)); // print the length of str2
    strcat (str1, str2); // append str2 to str1
    printf ("The concatenated string is %s\n", str1); // print the concatenated string
    strcpy (str3, str1); // copy str1 to str3
    printf ("The copied string is %s\n", str3); // print the copied string
    return 0; // return 0 to indicate successful execution
}
```