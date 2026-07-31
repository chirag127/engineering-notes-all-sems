Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write a program to implement strlen(), strcat(), and strcpy() using the concept of functions. Here is the content in markdown format:

## 28.WAP to implement strlen (), strcat (),strcpy () using the concept of Functions.

- The strlen() function returns the length of a string, excluding the null terminator. The function prototype is:

```c
int strlen(const char *s);
```

- The strcat() function appends a copy of the source string to the end of the destination string, and returns a pointer to the destination string. The function prototype is:

```c
char *strcat(char *dest, const char *src);
```

- The strcpy() function copies the source string to the destination string, and returns a pointer to the destination string. The function prototype is:

```c
char *strcpy(char *dest, const char *src);
```

- To implement these functions using the concept of functions, we can use the following steps:

  - Declare the function prototypes at the beginning of the program.
  - Define the functions below the main() function, using pointers and loops to manipulate the strings.
  - Call the functions from the main() function, passing the appropriate arguments and displaying the results.

- Here is an example program that implements these functions:

```c
#include <stdio.h>

// function prototypes
int strlen(const char *s);
char *strcat(char *dest, const char *src);
char *strcpy(char *dest, const char *src);

int main()
{
    // declare and initialize some strings
    char s1[20] = "Hello";
    char s2[20] = "World";
    char s3[20];

    // display the lengths of the strings
    printf("The length of s1 is %d\n", strlen(s1));
    printf("The length of s2 is %d\n", strlen(s2));
    printf("The length of s3 is %d\n", strlen(s3));

    // concatenate s1 and s2 and store the result in s3
    strcat(s3, s1);
    strcat(s3, s2);

    // display the contents of s3
    printf("The contents of s3 are %s\n", s3);

    // copy s2 to s1
    strcpy(s1, s2);

    // display the contents of s1 and s2
    printf("The contents of s1 are %s\n", s1);
    printf("The contents of s2 are %s\n", s2);

    return 0;
}

// function definitions

// returns the length of a string
int strlen(const char *s)
{
    // initialize a counter variable
    int count = 0;

    // loop through the string until the null terminator is reached
    while (*s != '\0')
    {
        // increment the counter
        count++;

        // move the pointer to the next character
        s++;
    }

    // return the counter value
    return count;
}

// appends a copy of the source string to the end of the destination string
char *strcat(char *dest, const char *src)
{
    // declare a pointer to store the original destination address
    char *temp = dest;

    // loop through the destination string until the null terminator is reached
    while (*dest != '\0')
    {
        // move the pointer to the next character
        dest++;
    }

    // loop through the source string until the null terminator is reached
    while (*src != '\0')
    {
        // copy the source character to the destination
        *dest = *src;

        // move both pointers to the next character
        dest++;
        src++;
    }

    // append a null terminator to the destination string
    *dest = '\0';

    // return the original destination address
    return temp;
}

// copies the source string to the destination string
char *strcpy(char *dest, const char *src)
{
    // declare a pointer to store the original destination address
    char *temp = dest;

    // loop through the source string until the null terminator is reached
    while (*src != '\0')
    {
        // copy the source character to the destination
        *dest = *src;

        // move both pointers to the next character
        dest++;
        src++;
    }

    // append a null terminator to the destination string
    *dest = '\0';

    // return the original destination address
    return temp;
}
```