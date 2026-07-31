## 23. WAP to find the minimum and maximum element of the array.

In programming, arrays are used to store a collection of similar type of data. It is often required to find the minimum and maximum element of an array. Here, we will discuss how to write a program in C++ to find the minimum and maximum element of an array.

### Algorithm

1. Declare an array of size n.
2. Initialize the array elements.
3. Declare two variables, min and max, and initialize them with the first element of the array.
4. Traverse the array from the second element to the last element.
5. If the current element is less than the min variable, update the min variable with the current element.
6. If the current element is greater than the max variable, update the max variable with the current element.
7. After traversing the whole array, print the values of min and max variables.

### Code

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the size of the array: ";
    cin >> n;

    int arr[n];
    cout << "Enter " << n << " elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int min = arr[0], max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    cout << "Minimum element of the array is: " << min << endl;
    cout << "Maximum element of the array is: " << max << endl;

    return 0;
}
```

### Explanation

1. The program starts by accepting the size of the array from the user.
2. An array of size n is declared and the user inputs n elements of the array.
3. Two variables, min and max, are declared and are initialized with the first element of the array.
4. The program then traverses through the array, starting from the second element to the last element.
5. If the current element is less than the min variable, the min variable is updated with the current element.
6. If the current element is greater than the max variable, the max variable is updated with the current element.
7. After traversing the whole array, the program prints the values of min and max variables.

### Conclusion

In this article, we have discussed how to write a program in C++ to find the minimum and maximum element of an array. By following the algorithm and understanding the code, one can easily find the minimum and maximum element of an array in C++.