## 30. WAP to swap two elements using the concept of pointers.

30. WAP to Swap Two Elements Using Pointers:

Pointers are variables that store memory addresses, and are often used in C programming to manipulate data stored in memory. To swap two elements using pointers, you can use the concept of pointers to pass the memory addresses of the elements to a function, and then use the function to swap the values stored at those addresses.

Here is an example of a C program to swap two elements using pointers:

```
#include <stdio.h>

void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

int main() {
  int x = 10, y = 20;
  printf("Before swapping: x = %d, y = %d\n", x, y);
  swap(&x, &y);
  printf("After swapping: x = %d, y = %d\n", x, y);
  return 0;
}
```

In this example, the `swap` function takes two pointers to `int` as arguments, and uses the pointers to swap the values stored at the addresses they point to. The `main` function declares two variables `x` and `y`, initializes them to 10 and 20, respectively, and then calls the `swap` function to swap their values.

In conclusion, to swap two elements using pointers, you can use the concept of pointers to pass the memory addresses of the elements to a function, and then use the function to swap the values stored at those addresses. This is a common technique in C programming for manipulating data stored in memory, and can be used to implement a wide range of algorithms and data structures.
