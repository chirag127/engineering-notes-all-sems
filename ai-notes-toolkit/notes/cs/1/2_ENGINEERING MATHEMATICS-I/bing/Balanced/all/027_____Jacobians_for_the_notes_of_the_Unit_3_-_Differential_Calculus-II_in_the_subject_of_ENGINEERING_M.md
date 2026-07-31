# Jacobians

- A Jacobian is a determinant or a matrix that is defined for a finite number of functions of the same number of variables .
- Each row of the Jacobian matrix consists of the first partial derivatives of the same function with respect to each of the variables  .
- The Jacobian determinant is the determinant of the Jacobian matrix and is denoted by J .
- The Jacobian matrix and determinant are useful for studying the properties of transformations, such as linearity, invertibility, and change of variables .

## Example of Jacobian matrix and determinant

- Suppose u and v are functions of the two independent variables x and y, then the Jacobian matrix of u and v with respect to x and y is given by :

```
J = | du/dx  du/dy |
    | dv/dx  dv/dy |
```

- The Jacobian determinant of u and v with respect to x and y is given by :

```
J = | du/dx  du/dy |
    | dv/dx  dv/dy |

  = (du/dx)(dv/dy) - (du/dy)(dv/dx)
```

## Properties of Jacobian

- The Jacobian of a linear transformation is a constant.
- The Jacobian of an inverse transformation is the reciprocal of the Jacobian of the original transformation.
- The Jacobian of a composite transformation is the product of the Jacobians of the individual transformations.
- The Jacobian of a transformation is zero if and only if the transformation is singular, i.e., not one-to-one.
- The Jacobian of a transformation measures the factor by which the transformation changes the area (or volume) of a region .