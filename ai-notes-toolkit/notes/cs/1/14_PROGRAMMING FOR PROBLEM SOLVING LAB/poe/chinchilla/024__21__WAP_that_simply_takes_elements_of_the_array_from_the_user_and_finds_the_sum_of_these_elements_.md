## 21. WAP that simply takes elements of the array from the user and finds the sum of these elements.

Arrays are an essential data structure in programming, and many programs involve performing operations on arrays. In this section, we will learn how to write a program that takes elements of an array from the user and finds the sum of these elements.

Here are the steps to write a program that takes elements of an array from the user and finds the sum of these elements:

1. Firstly, we need to declare an array. We can do this by using the following syntax:

```c
datatype arrayName[arraySize];
```

Here `datatype` refers to the data type of the elements that the array will store, `arrayName` refers to the name of the array, and `arraySize` refers to the number of elements that the array can store.

2. Next, we will ask the user to enter the elements of the array. We can do this by using a loop and the `scanf()` function. Here's an example:

```c
for (int i = 0; i < arraySize; i++) {
    printf("Enter element %d: ", i+1);
    scanf("%d", &arrayName[i]);
}
```

In this example, we are using a `for` loop to iterate through the array and the `scanf()` function to read the user input. We are also using `i+1` to display the element number to the user.

3. Once we have read the elements of the array, we can calculate the sum of these elements. We can do this by using another loop to iterate through the array and adding each element to a variable that stores the sum. Here's an example:

```c
int sum = 0;
for (int i = 0; i < arraySize; i++) {
    sum += arrayName[i];
}
printf("The sum is: %d", sum);
```

In this example, we are using a `for` loop to iterate through the array and the `+=` operator to add each element to the `sum` variable. Finally, we are using the `printf()` function to display the sum to the user.

4. Finally, we can put all these steps together to create a complete program. Here's the full code:

```c
#include <stdio.h>

int main() {
    int arraySize;
    printf("Enter the size of the array: ");
    scanf("%d", &arraySize);

    int arrayName[arraySize];
    for (int i = 0; i < arraySize; i++) {
        printf("Enter element %d: ", i+1);
        scanf("%d", &arrayName[i]);
    }

    int sum = 0;
    for (int i = 0; i < arraySize; i++) {
        sum += arrayName[i];
    }
    printf("The sum is: %d", sum);

    return 0;
}
```

In this example, we are declaring the array, reading the elements of the array from the user, calculating the sum of the elements, and displaying the sum to the user.

In conclusion, arrays are a powerful data structure in programming, and we can perform many operations on arrays, including finding the sum of the elements. By following the steps outlined above, we can write a program that takes elements of an array from the user and finds the sum of these elements.