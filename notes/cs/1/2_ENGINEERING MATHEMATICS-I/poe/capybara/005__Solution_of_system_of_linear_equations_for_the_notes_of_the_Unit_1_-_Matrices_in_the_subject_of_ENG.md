### Solution of System of Linear Equations

Linear equations are equations that involve only linear terms. A system of linear equations is a collection of two or more linear equations involving the same set of variables. In this unit, we will learn about the solution of a system of linear equations using matrices.

#### Augmented Matrix

An augmented matrix is a matrix formed by appending the columns of a given matrix to the right of an identity matrix of the same number of rows. The augmented matrix is used to solve a system of linear equations.

#### Gauss-Jordan Elimination Method

The Gauss-Jordan elimination method is used to solve a system of linear equations by converting the augmented matrix into a reduced row echelon form. The steps involved in the method are:

1. Write the augmented matrix of the system of linear equations.
2. Use row operations to convert the matrix into a reduced row echelon form.
3. Interpret the reduced row echelon form to obtain the solution of the system of linear equations.

#### Gauss-Jordan Elimination Method Example

Consider the following system of linear equations:

```
2x + 3y - z = 1
x - y + z = 2
3x + 2y - 2z = 3
```

The augmented matrix of the system is:

```
[ 2  3 -1 | 1 ]
[ 1 -1  1 | 2 ]
[ 3  2 -2 | 3 ]
```

Using row operations, we can convert the augmented matrix into a reduced row echelon form:

```
[ 1  0  0 | 1 ]
[ 0  1  0 | 0 ]
[ 0  0  1 | -1 ]
```

The reduced row echelon form of the augmented matrix tells us that the solution of the system of linear equations is:

```
x = 1
y = 0
z = -1
```

#### Cramer's Rule

Cramer's rule is a method used to solve a system of linear equations using determinants. The steps involved in the method are:

1. Write the augmented matrix of the system of linear equations.
2. Determine the determinant of the coefficient matrix.
3. Replace each column of the coefficient matrix with the column of constants and determine the determinant.
4. The solution of the system of linear equations is obtained by dividing the determinant of each column by the determinant of the coefficient matrix.

#### Cramer's Rule Example

Consider the following system of linear equations:

```
2x + 3y - z = 1
x - y + z = 2
3x + 2y - 2z = 3
```

The coefficient matrix of the system is:

```
[ 2  3 -1 ]
[ 1 -1  1 ]
[ 3  2 -2 ]
```

The determinant of the coefficient matrix is:

```
| 2  3 -1 |
| 1 -1  1 |
| 3  2 -2 | = 15
```

The determinant of the matrix obtained by replacing the first column of the coefficient matrix with the column of constants is:

```
| 1  3 -1 |
| 2 -1  1 |
| 3  3 -2 | = -10
```

Similarly, the determinants of the matrices obtained by replacing the second and third columns of the coefficient matrix with the columns of constants are:

```
| 2  1 -1 |
| 1  2  1 |
| 3  3  3 | = 12
```

and

```
| 2  3  1 |
| 1 -1  2 |
| 3  2  3 | = -9
```

The solution of the system of linear equations is:

```
x = -2/5
y = 2/5
z = -1/5
```