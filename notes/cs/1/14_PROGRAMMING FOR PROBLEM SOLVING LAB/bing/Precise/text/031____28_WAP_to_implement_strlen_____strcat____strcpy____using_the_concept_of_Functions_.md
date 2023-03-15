## 28. WAP to implement strlen(), strcat(), strcpy() using the concept of Functions

`strlen()` is a function that returns the length of a string. It takes a single argument, which is a pointer to the first character of the string. The function counts the number of characters in the string until it reaches the null character, which marks the end of the string.

Here is an example of how to implement `strlen()` using the concept of functions:

```c
#include <stdio.h>

int my_strlen(char *str) {
    int length = 0;
    while (*str != '\0') {
        length++;
        str++;
    }
    return length;
}

int main() {
    char str[] = "Hello, world!";
    printf("Length of string: %d\n", my_strlen(str));
    return 0;
}
```

`strcat()` is a function that concatenates two strings. It takes two arguments: the first is a pointer to the destination string, and the second is a pointer to the source string. The function appends the source string to the destination string.

Here is an example of how to implement `strcat()` using the concept of functions:

```c
#include <stdio.h>

void my_strcat(char *dest, char *src) {
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
    char dest[20] = "Hello, ";
    char src[] = "world!";
    my_strcat(dest, src);
    printf("Concatenated string: %s\n", dest);
    return 0;
}
```

`strcpy()` is a function that copies a string. It takes two arguments: the first is a pointer to the destination string, and the second is a pointer to the source string. The function copies the source string to the destination string.

Here is an example of how to implement `strcpy()` using the concept of functions:

```c
#include <stdio.h>

void my_strcpy(char *dest, char *src) {
    while (*src != '\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';
}

int main() {
    char src[] = "Hello, world!";
    char dest[20];
    my_strcpy(dest, src);
    printf("Copied string: %s\n", dest);
    return 0;
}
```