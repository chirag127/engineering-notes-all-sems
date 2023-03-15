## 28. WAP to implement strlen(), strcat(), strcpy() using the concept of Functions

`strlen()` is a function that returns the length of a string. It takes a single argument, which is the string whose length is to be determined. The function returns an integer value representing the number of characters in the string.

`strcat()` is a function that concatenates two strings. It takes two arguments, the first is the destination string and the second is the source string. The function appends the source string to the destination string and returns a pointer to the destination string.

`strcpy()` is a function that copies a string. It takes two arguments, the first is the destination string and the second is the source string. The function copies the source string to the destination string and returns a pointer to the destination string.

Here is an example of how these functions can be implemented using the concept of functions in C:

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

void my_strcpy(char *dest, char *src) {
    while (*src != '\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';
}

int main() {
    char str1[100] = "Hello";
    char str2[100] = "World";
    printf("Length of str1: %d\n", my_strlen(str1));
    my_strcat(str1, str2);
    printf("str1 after concatenation: %s\n", str1);
    my_strcpy(str1, str2);
    printf("str1 after copying: %s\n", str1);
    return 0;
}
```

This program defines three functions, `my_strlen()`, `my_strcat()`, and `my_strcpy()`, which implement the functionality of the `strlen()`, `strcat()`, and `strcpy()` functions, respectively. The `main()` function demonstrates how these functions can be used. It first declares two strings, `str1` and `str2`, and initializes them with the values "Hello" and "World", respectively. It then uses the `my_strlen()` function to determine the length of `str1` and prints the result. Next, it uses the `my_strcat()` function to concatenate `str2` to `str1` and prints the result. Finally, it uses the `my_strcpy()` function to copy `str2` to `str1` and prints the result.