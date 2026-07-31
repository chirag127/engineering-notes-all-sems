 Here is the formal content in markdown format without any emojis or external links:

## 22.WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.

1. Take input for size of arrays:

`size = int(input("Enter size of arrays: "))`

2. Take input for first array elements:

`arr1 = [int(input()) for x in range(size)]`

3. Take input for second array elements:

`arr2 = [int(input()) for x in range(size)]`

4. Create a third array to store sum of corresponding elements:

`arr3 = [None] * size`

5. Loop to calculate sum and store in third array:

`for i in range(size):`

`arr3[i] = arr1[i] + arr2[i]`

6. Print the third array:

`print(arr3)`

The above program takes input for size of two arrays. Then, it takes input for elements of two arrays. A third array is created to store sum of corresponding elements. A loop calculates sum of corresponding elements and stores in third array. Finally, the third array is printed.