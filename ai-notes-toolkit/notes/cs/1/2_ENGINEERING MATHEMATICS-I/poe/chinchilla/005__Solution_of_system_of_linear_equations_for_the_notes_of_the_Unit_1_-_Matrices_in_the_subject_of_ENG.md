

### Solution of System of Linear Equations

Linear equations play a crucial role in engineering mathematics. A system of linear equations is a set of equations that can be solved simultaneously. Let's delve deeper into the solution of a system of linear equations.

1. Matrix Representation: A system of linear equations can be represented in matrix form. The coefficients of the variables are put in a matrix called the coefficient matrix. The variables are put in a matrix called the variable matrix. The constants are put in a matrix called the constant matrix. 

2. Augmented Matrix: The augmented matrix of a system of linear equations is the matrix formed by augmenting the coefficient matrix and the constant matrix. 

3. Elementary Row Operations: Elementary Row Operations (EROs) are used to transform the augmented matrix into a form that is easier to solve. The three types of EROs are: 
    - Interchange two rows
    - Multiply a row by a non-zero scalar
    - Add a multiple of one row to another row

4. Row Echelon Form: An augmented matrix is said to be in Row Echelon Form (REF) if: 
    - All non-zero rows are above any rows of all zeros
    - The leading coefficient of a non-zero row is always strictly to the right of the leading coefficient of the row above it
    - All entries in a column below a leading coefficient are zeros

5. Reduced Row Echelon Form: An augmented matrix is said to be in Reduced Row Echelon Form (RREF) if: 
    - It is in REF
    - Every leading coefficient is 1
    - The only non-zero entry in each column with a leading coefficient is the leading coefficient

6. Solution: Once the augmented matrix is in RREF, we can easily solve for the variables. If there are n variables, then the RREF will have n columns. The variables will correspond to the columns that have a leading coefficient of 1. The values of the variables can be found by back-substitution. 

In conclusion, the solution of a system of linear equations involves representing the equations in matrix form, transforming the augmented matrix using EROs to REF and RREF, and finally solving for the variables using back-substitution.