## 28. WAP to implement strlen(), strcat(), strcpy() using the concept of Functions

`strlen()`, `strcat()`, and `strcpy()` are all functions in the C programming language that operate on strings. Here is an example of how to implement these functions using the concept of functions:

1. `strlen()` function: This function returns the length of a string. Here is an example of how to implement this function:

```c
#include <stdio.h>

int strlen(char *str) {
    int length = 0;
    while (*str != '\0') {
        length++;
        str++;
    }
    return length;
}
```

2. `strcat()` function: This function concatenates two strings. Here is an example of how to implement this function:

```c
#include <stdio.h>

void strcat(char *dest, char *src) {
    while (*dest != '\0') {
        dest++;
    }
    while (*src != '\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';
}
```

3. `strcpy()` function: This function copies a string from one location to another. Here is an example of how to implement this function:

```c
#include <stdio.h>

void strcpy(char *dest, char *src) {
    while (*src != '\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';
}
```

These are the basic implementations of the `strlen()`, `strcat()`, and `strcpy()` functions using the concept of functions in C programming language. These functions can be further optimized and improved based on specific requirements.