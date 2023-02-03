## 26.WAP to add and multiply two matrices of order nxn.

To add and multiply two matrices of order nxn, you can write a program in a programming language such as C++, Python, or Java. The following steps can be followed to write a program to add and multiply two matrices:

1. Define the size of the matrices (nxn).

2. Create two matrices of size nxn and fill them with values.

3. Create a third matrix of size nxn to store the result of the addition or multiplication.

4. Implement a loop to iterate over the elements of the matrices and perform the addition or multiplication operation.

5. For addition, add the corresponding elements of the two matrices and store the result in the third matrix.

6. For multiplication, multiply the elements of the first matrix by the elements of the second matrix and store the result in the third matrix.

7. Print the result matrix to the screen.

Here is an example of a program in C++ to add two matrices of size nxn:

#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Enter the size of the matrices (nxn): ";
    cin >> n;
    
    int a[n][n], b[n][n], c[n][n];
    
    cout << "Enter the elements of the first matrix: " << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> a[i][j];
        }
    }
    
    cout << "Enter the elements of the second matrix: " << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> b[i][j];
        }
    }
    
    cout << "The result of adding the matrices is: " << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            c[i][j] = a[i][j] + b[i][j];
            cout << c[i][j] << " ";
        }
        cout << endl;
    }
    
    return 0;
}

This program takes as input the size of the matrices and the elements of the matrices, and outputs the result of adding the matrices. You can modify the program to multiply the matrices by changing the operation in the loop.
