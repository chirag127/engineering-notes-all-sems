## 28. WAP to implement strlen (), strcat (), strcpy () using the concept of Functions

To implement string functions like strlen(), strcat(), and strcpy() using the concept of functions, we can follow the below steps:

1. Declare a function for each of the string functions that we want to implement. For example, for strlen() function, we can declare a function like:

```c
int my_strlen(char *str);
```

Similarly, we can declare functions for strcat() and strcpy() functions as well.

2. Implement the functions by writing the code for each function. For example, to implement my_strlen() function, we can write the code like:

```c
int my_strlen(char *str) {
    int len = 0;
    while(*str != '\0') {
        len++;
        str++;
    }
    return len;
}
```

This code will iterate through the string character by character until it encounters the null character '\0'. It will keep incrementing the length variable and the pointer to the next character until the null character is encountered. Finally, it will return the length of the string.

3. Similarly, we can implement the strcat() and strcpy() functions using the concept of functions. The code for my_strcat() function can be written like:

```c
char* my_strcat(char *dest, char *src) {
    while(*dest != '\0') {
        dest++;
    }
    while(*src != '\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';
    return dest;
}
```

This code will iterate through the destination string until it encounters the null character '\0'. Then, it will copy the characters from the source string to the destination string until the null character is encountered in the source string. Finally, it will append the null character at the end of the destination string.

4. The code for my_strcpy() function can be written like:

```c
char* my_strcpy(char *dest, char *src) {
    while(*src != '\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';
    return dest;
}
```

This code will copy the characters from the source string to the destination string until the null character is encountered in the source string. Finally, it will append the null character at the end of the destination string.

By implementing these string functions using the concept of functions, we can reuse the code and make our program more modular and efficient.