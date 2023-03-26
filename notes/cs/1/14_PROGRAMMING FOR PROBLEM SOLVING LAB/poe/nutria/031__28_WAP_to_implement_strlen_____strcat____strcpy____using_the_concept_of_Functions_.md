

## 28.WAP to implement strlen (), strcat (),strcpy () using the concept of Functions

* `strlen()` is a function used to determine the length of a string. It takes a string as an argument and returns the length of the string as an integer.
* `strcat()` is a function used to concatenate two strings together. It takes two strings as arguments and returns a new string that is the combination of the two strings.
* `strcpy()` is a function used to copy one string to another. It takes two strings as arguments and copies the first string to the second string.

To implement these functions using the concept of functions, we must first define the functions. The syntax for defining a function is:

```
return_type function_name (parameters) {
  // code for the function
}
```

For `strlen()`, the return type is an integer and the parameters are a string. The code for the function should loop through the string and increment a counter for each character in the string. The function should then return the counter.

For `strcat()`, the return type is a string and the parameters are two strings. The code for the function should loop through the first string and concatenate each character to the second string. The function should then return the concatenated string.

For `strcpy()`, the return type is a string and the parameters are two strings. The code for the function should loop through the first string and copy each character to the second string. The function should then return the copied string.