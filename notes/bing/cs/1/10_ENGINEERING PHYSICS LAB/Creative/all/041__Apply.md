#### Apply

- Apply is a function in R programming that allows you to apply a function to the rows or columns of a matrix or data frame, or to a list or vector.
- The syntax of apply is `apply(X, MARGIN, FUN, ...)`, where
  - X is the object to be processed
  - MARGIN is a vector indicating the dimensions to use: 1 for rows, 2 for columns, or c(1,2) for both
  - FUN is the function to be applied
  - ... are optional arguments to be passed to FUN
- Apply is useful for performing operations that require looping over the elements of an object, such as calculating row or column sums, means, standard deviations, etc.
- Apply can also be used to apply user-defined functions to an object, as long as the function returns a vector of the same length for each input.
- Some examples of using apply are:

  - To calculate the row sums of a matrix:

    ```r
    # create a 3x4 matrix of random numbers
    mat <- matrix(runif(12), nrow = 3)
    mat
    #>           [,1]      [,2]      [,3]      [,4]
    #> [1,] 0.9347052 0.4820801 0.8209463 0.4776196
    #> [2,] 0.2121425 0.5995658 0.6470602 0.7323137
    #> [3,] 0.6516738 0.4935413 0.7829326 0.1680519
    # apply the sum function to the rows (MARGIN = 1)
    apply(mat, 1, sum)
    #> [1] 2.715351 2.191082 2.096200
    ```

  - To calculate the column means of a data frame:

    ```r
    # create a data frame of 5 observations and 3 variables
    df <- data.frame(x = rnorm(5), y = rpois(5, 2), z = rbinom(5, 10, 0.5))
    df
    #>            x y z
    #> 1 -0.1557950 1 4
    #> 2  0.1814413 1 6
    #> 3  0.5269876 4 6
    #> 4 -0.2358358 3 5
    #> 5 -0.4534971 1 4
    # apply the mean function to the columns (MARGIN = 2)
    apply(df, 2, mean)
    #>          x          y          z 
    #> -0.0273398  2.0000000  5.0000000
    ```

  - To apply a user-defined function to a list:

    ```r
    # create a list of 3 vectors of different lengths
    lst <- list(a = 1:5, b = 6:10, c = 11:15)
    lst
    #> $a
    #> [1] 1 2 3 4 5
    #> 
    #> $b
    #> [1]  6  7  8  9 10
    #> 
    #> $c
    #> [1] 11 12 13 14 15
    # define a function that returns the first and last elements of a vector
    first_last <- function(x) {
      c(first = x[1], last = x[length(x)])
    }
    # apply the function to the list
    apply(lst, 2, first_last)
    #>      a  b  c
    #> first 1  6 11
    #> last  5 10 15
    ```