## 23. WAP to find the minimum and maximum element of the array

Here is an example of a program that finds the minimum and maximum element of an array in C++:

```c++
#include<iostream>
using namespace std;
int main()
{
    int n, i, max, min;
    cout<<"Enter the size of the array: ";
    cin>>n;
    int arr[n];
    cout<<"Enter the elements of the array: ";
    for(i=0; i<n; i++)
    {
        cin>>arr[i];
    }
    max = arr[0];
    min = arr[0];
    for(i=0; i<n; i++)
    {
        if(arr[i]>max)
            max = arr[i];
        if(arr[i]<min)
            min = arr[i];
    }
    cout<<"The maximum element of the array is: "<<max<<endl;
    cout<<"The minimum element of the array is: "<<min<<endl;
    return 0;
}
```

This program prompts the user to enter the size of the array and its elements. It then initializes the `max` and `min` variables to the first element of the array. The program then iterates through the array, comparing each element to the current `max` and `min` values. If an element is greater than the current `max` value, it is assigned to `max`. If an element is less than the current `min` value, it is assigned to `min`. Finally, the program outputs the maximum and minimum elements of the array.

- This program can be modified to work with different data types and to handle different input methods.
- The time complexity of this program is O(n), where n is the size of the array.
- The space complexity of this program is O(1), as it uses a constant amount of additional space.