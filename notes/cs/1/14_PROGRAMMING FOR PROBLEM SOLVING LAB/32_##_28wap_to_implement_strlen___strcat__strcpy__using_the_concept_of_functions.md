## 28.WAP to implement strlen (), strcat (),strcpy () using the concept of Functions.

28. Implementation of strlen (), strcat (), strcpy () Functions:

In the C programming language, strlen (), strcat (), and strcpy () are functions that are used to manipulate strings. These functions can be implemented using the concept of functions in C.

1. strlen () function: The strlen () function is used to find the length of a string. The function takes a string as an argument and returns the number of characters in the string, excluding the null terminator. The implementation of the strlen () function can be as follows:

```
int strlen (char *s) {
    int length = 0;
    while (*s != '\0') {
        length++;
        s++;
    }
    return length;
}
```

2. strcat () function: The strcat () function is used to concatenate two strings. The function takes two strings as arguments and appends the second string to the end of the first string. The implementation of the strcat () function can be as follows:

```
char *strcat (char *dest, const char *src) {
    char *ptr = dest;
    while (*dest) {
        dest++;
    }
    while (*src) {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';
    return ptr;
}
```

3. strcpy () function: The strcpy () function is used to copy a string. The function takes two strings as arguments and copies the content of the second string to the first string. The implementation of the strcpy () function can be as follows:

```
char *strcpy (char *dest, const char *src) {
    char *ptr = dest;
    while (*src) {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';
    return ptr;
}
```

In conclusion, strlen (), strcat (), and strcpy () are functions that are used to manipulate strings in the C programming language. These functions can be implemented using the concept of functions in C, and the implementation of these functions involves using pointers and looping constructs to manipulate the strings. Understanding the implementation of these functions is important for working with strings in C.
