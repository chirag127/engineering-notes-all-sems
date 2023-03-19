## 28.WAP to implement strlen (), strcat (),strcpy () using the concept of Functions.

When working with strings in C programming language, it is often necessary to perform operations such as finding the length of a string, copying one string to another, or concatenating two strings together. These operations can be achieved using the built-in string functions provided by the language, such as strlen(), strcat(), and strcpy(). However, it is also possible to implement these functions using the concept of functions in C programming.

In this study material, we will learn how to implement strlen(), strcat(), and strcpy() functions using the concept of functions in C programming.

### 1. Implementing strlen() function using functions in C

The strlen() function in C is used to find the length of a string. To implement this function using functions, we can define a function that takes a string as input and counts the number of characters in the string until it reaches the null character '\0'. The steps to implement strlen() function using functions in C are as follows:

- Define a function called mystrlen() that takes a string as input.
- Initialize a counter variable to 0.
- Use a while loop to iterate through the string until the null character '\0' is reached.
- Increment the counter variable for each character in the string.
- Return the counter variable as the length of the string.

```c
int mystrlen(char str[]) {
    int length = 0;
    while(str[length] != '\0') {
        length++;
    }
    return length;
}
```

### 2. Implementing strcat() function using functions in C

The strcat() function in C is used to concatenate (join) two strings together. To implement this function using functions, we can define a function that takes two strings as input and appends the second string to the end of the first string. The steps to implement strcat() function using functions in C are as follows:

- Define a function called mystrcat() that takes two strings as input.
- Find the length of the first string using the mystrlen() function defined earlier.
- Use a for loop to append each character in the second string to the end of the first string.
- Add the null character '\0' at the end of the concatenated string.
- Return the concatenated string.

```c
char* mystrcat(char str1[], char str2[]) {
    int i, j;
    i = mystrlen(str1);
    for(j = 0; str2[j] != '\0'; j++) {
        str1[i++] = str2[j];
    }
    str1[i] = '\0';
    return str1;
}
```

### 3. Implementing strcpy() function using functions in C

The strcpy() function in C is used to copy one string to another. To implement this function using functions, we can define a function that takes two strings as input and copies the contents of the second string to the first string. The steps to implement strcpy() function using functions in C are as follows:

- Define a function called mystrcpy() that takes two strings as input.
- Use a for loop to copy each character in the second string to the first string.
- Add the null character '\0' at the end of the copied string.
- Return the copied string.

```c
char* mystrcpy(char str1[], char str2[]) {
    int i;
    for(i = 0; str2[i] != '\0'; i++) {
        str1[i] = str2[i];
    }
    str1[i] = '\0';
    return str1;
}
```

By implementing these string functions using functions in C programming, we can have a better understanding of how these functions work internally. It also allows us to customize these functions according to our specific needs.