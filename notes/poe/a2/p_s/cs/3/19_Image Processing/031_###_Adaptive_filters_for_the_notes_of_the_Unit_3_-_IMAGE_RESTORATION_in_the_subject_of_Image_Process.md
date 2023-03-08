 Here is the content in markdown format for the given topic:

### Adaptive filters for the notes of the Unit 3 - IMAGE RESTORATION

- Adaptive filters are a type of filters whose parameters are automatically adjusted based on the input signal statistics.
- They are used in image restoration to remove noise and blurring effects from images.
- The filter parameters are adjusted iteratively based on the error between the actual output and the desired output.
- This makes adaptive filters flexible and useful for non-stationary signals like images where statistics keep changing.
- Some types of adaptive filters are:
    - Least Mean Square (LMS) filter: Parameters are adjusted to minimize the mean square error.
    - Recursive Least Squares (RLS) filter: Parameters are adjusted to minimize the least squares error in a recursive manner.
- Advantages:
    - Can handle non-stationary inputs.
    - Does not require prior knowledge of signal statistics.
- Disadvantages:
    - Can be complex to implement.
    - Convergence is not guaranteed and can be slow.
- Applications:
    - Image deblurring.
    - Image noise removal.
    - Image enhancement.

- Here is an ascii diagram showing the basic structure of an adaptive filter:

        +