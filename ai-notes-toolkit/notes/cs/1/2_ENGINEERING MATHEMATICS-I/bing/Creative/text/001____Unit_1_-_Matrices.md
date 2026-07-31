## Unit 1 - Matrices

- A matrix is a rectangular array of numbers, symbols, or expressions, arranged in rows and columns.
- The size or order of a matrix is defined by the number of rows and columns it has. For example, a matrix with 3 rows and 2 columns has the order 3 x 2.
- The entries or elements of a matrix are the numbers, symbols, or expressions that occupy each cell of the matrix. They are usually denoted by lowercase letters with subscripts indicating their row and column positions. For example, a<sub>2,1</sub> is the element in the second row and first column of matrix A.
- A matrix can be represented by enclosing its elements in square brackets [ ] or parentheses ( ). For example, the matrix A with order 2 x 3 can be written as:

  A = [a<sub>1,1</sub> a<sub>1,2</sub> a<sub>1,3</sub>  
       a<sub>2,1</sub> a<sub>2,2</sub> a<sub>2,3</sub>]

  or

  A = (a<sub>1,1</sub> a<sub>1,2</sub> a<sub>1,3</sub>  
       a<sub>2,1</sub> a<sub>2,2</sub> a<sub>2,3</sub>)

- A matrix can also be represented by using a capital letter to denote its name and a lowercase letter to denote its elements. For example, the matrix A can be written as:

  A = [a<sub>ij</sub>] where i = 1, 2 and j = 1, 2, 3

  This means that a<sub>ij</sub> is the element in the i<sup>th</sup> row and j<sup>th</sup> column of matrix A.

- There are different types of matrices based on their properties and applications. Some common types are:

  - A square matrix is a matrix that has the same number of rows and columns. For example, a matrix with order 2 x 2 or 3 x 3 is a square matrix.
  - A diagonal matrix is a square matrix that has non-zero elements only on its main diagonal, which runs from the top left to the bottom right corner. For example, the matrix D with order 3 x 3 is a diagonal matrix:

    D = [d<sub>1,1</sub> 0 0  
         0 d<sub>2,2</sub> 0  
         0 0 d<sub>3,3</sub>]

  - A scalar matrix is a diagonal matrix that has the same non-zero element on its main diagonal. For example, the matrix S with order 2 x 2 is a scalar matrix:

    S = [k 0  
         0 k]

    where k is any constant.

  - An identity matrix is a scalar matrix that has 1 as its main diagonal element. It is denoted by I or I<sub>n</sub>, where n is the order of the matrix. For example, the matrix I with order 3 x 3 is an identity matrix:

    I = [1 0 0  
         0 1 0  
         0 0 1]

  - A zero matrix is a matrix that has all its elements equal to zero. It is denoted by O or O<sub>m,n</sub>, where m and n are the number of rows and columns of the matrix. For example, the matrix O with order 2 x 3 is a zero matrix:

    O = [0 0 0  
         0 0 0]

  - A row matrix is a matrix that has only one row. For example, the matrix R with order 1 x 3 is a row matrix:

    R = [r<sub>1</sub> r<sub>2</sub> r<sub>3</sub>]

  - A column matrix is a matrix that has only one column. For example, the matrix C with order 3 x 1 is a column matrix:

    C = [c<sub>1</sub>  
         c<sub>2</sub>  
         c<sub>3</sub>]

  - A transpose of a matrix is a matrix that is obtained by interchanging the rows and columns of the original matrix. It is denoted by A<sup>T</sup> or A'.