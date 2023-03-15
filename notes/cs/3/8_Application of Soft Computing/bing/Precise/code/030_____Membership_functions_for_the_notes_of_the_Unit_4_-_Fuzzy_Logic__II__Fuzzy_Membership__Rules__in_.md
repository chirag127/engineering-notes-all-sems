### Membership Functions

Membership functions are used in fuzzy logic to represent the degree of truth of a statement. They are used to map the input values to a degree of membership in a fuzzy set. The shape of the membership function determines how the input values are mapped to the degree of membership.

Some common types of membership functions are:

1. Triangular membership function: This function is defined by three points, a, b, and c, and takes the shape of a triangle. The degree of membership is 0 outside the interval [a, c] and increases linearly from 0 to 1 in the interval [a, b] and decreases linearly from 1 to 0 in the interval [b, c].

2. Trapezoidal membership function: This function is defined by four points, a, b, c, and d, and takes the shape of a trapezoid. The degree of membership is 0 outside the interval [a, d] and increases linearly from 0 to 1 in the interval [a, b], remains constant at 1 in the interval [b, c], and decreases linearly from 1 to 0 in the interval [c, d].

3. Gaussian membership function: This function is defined by two parameters, the mean μ and the standard deviation σ, and takes the shape of a bell curve. The degree of membership is given by the formula exp(-((x-μ)/σ)^2).

4. Sigmoidal membership function: This function is defined by two parameters, the slope a and the midpoint c, and takes the shape of an S-curve. The degree of membership is given by the formula 1/(1+exp(-a(x-c))).

These are some of the common membership functions used in fuzzy logic. The choice of membership function depends on the specific application and the nature of the input data. It is important to choose the appropriate membership function to accurately represent the degree of truth of a statement.