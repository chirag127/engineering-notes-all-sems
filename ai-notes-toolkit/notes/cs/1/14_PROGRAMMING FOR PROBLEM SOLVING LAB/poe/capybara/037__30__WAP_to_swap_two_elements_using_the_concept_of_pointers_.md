## 30. WAP to swap two elements using the concept of pointers

To swap two elements using pointers, we need to follow the following steps:

1. Declare two variables of the same data type that we want to swap.
2. Declare two pointer variables of the same data type.
3. Assign the addresses of the variables to the pointer variables.
4. Use **temporary variable** to swap the values.

Here is the code to swap two elements using pointers:

```c
#include <stdio.h>
void swap(int *x, int *y)
{
  int temp;
  temp = *x;
  *x = *y;
  *y = temp;
}
int main()
{
  int a, b;
  printf("Enter the value of a and b\n");
  scanf("%d%d", &a, &b);
  printf("Before Swapping\na = %d\nb = %d\n", a, b);
  swap(&a, &b);
  printf("After Swapping\na = %d\nb = %d\n", a, b);
  return 0;
}
```

In the above code, we declare two variables `a` and `b` of the same data type, which we want to swap. We declare two pointer variables `*x` and `*y` of the same data type as `a` and `b`. We assign the addresses of the variables `a` and `b` to the pointer variables `*x` and `*y`. We use a temporary variable `temp` to swap the values of `a` and `b`.

We call the `swap` function by passing the addresses of `a` and `b` as arguments. The `swap` function swaps the values of `a` and `b` using pointer variables `*x` and `*y`. Finally, we print the swapped values of `a` and `b`.

In conclusion, using the concept of pointers, we can easily swap two elements in C. We can define a separate function for swapping, or we can swap the values directly in the main function.