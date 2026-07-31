## 28. WAP to implement strlen(), strcat(), strcpy() using the concept of Functions

`strlen()`, `strcat()`, and `strcpy()` are all functions that can be implemented using the concept of functions in programming. Here is an explanation of each function and how they can be implemented:

1. `strlen()`: This function is used to find the length of a string. It takes a string as an argument and returns the number of characters in the string. Here is an example of how `strlen()` can be implemented:

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

int main() {
    char str[] = "Hello, World!";
    printf("Length of string: %d\n", strlen(str));
    return 0;
}
```

2. `strcat()`: This function is used to concatenate two strings. It takes two strings as arguments and appends the second string to the end of the first string. Here is an example of how `strcat()` can be implemented:

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

int main() {
    char str1[20] = "Hello, ";
    char str2[] = "World!";
    strcat(str1, str2);
    printf("Concatenated string: %s\n", str1);
    return 0;
}
```

3. `strcpy()`: This function is used to copy a string. It takes two strings as arguments and copies the second string into the first string. Here is an example of how `strcpy()` can be implemented:

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

int main() {
    char str1[20];
    char str2[] = "Hello, World!";
    strcpy(str1, str2);
    printf("Copied string: %s\n", str1);
    return 0;
}
```