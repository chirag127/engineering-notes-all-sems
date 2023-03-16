### Membership Functions

A membership function is a curve that defines how each point in the input space is mapped to a membership value between 0 and 1. The input space is sometimes referred to as the universe of discourse, and the curve is generally referred to as a membership function. Membership functions are used to quantify linguistic terms, and can be represented as mathematical functions or lookup tables.

There are several common shapes for membership functions, including triangular, trapezoidal, Gaussian, and sigmoidal. The choice of membership function shape depends on the nature of the input variable and the level of granularity desired in the fuzzy system.

Triangular membership functions are defined by three parameters: a, b, and c, where a and c define the "feet" of the triangle and b defines the peak. The membership function is 0 for values less than a and greater than c, and increases linearly from 0 to 1 between a and b, and decreases linearly from 1 to 0 between b and c.

Trapezoidal membership functions are similar to triangular membership functions, but have a flat top. They are defined by four parameters: a, b, c, and d, where a and d define the "feet" of the trapezoid, b and c define the "shoulders," and the membership function is 1 between b and c. The membership function is 0 for values less than a and greater than d, and increases linearly from 0 to 1 between a and b, and decreases linearly from 1 to 0 between c and d.

Gaussian membership functions have a bell shape and are defined by two parameters: c and σ, where c is the center of the bell and σ controls the width. The membership function is given by the equation exp(-(x-c)^2/(2σ^2)).

Sigmoidal membership functions have an S shape and are defined by two parameters: a and c, where a controls the slope of the curve and c is the inflection point. The membership function is given by the equation 1/(1+exp(-a(x-c))).

In summary, membership functions are used to represent linguistic terms in a fuzzy system, and can take on a variety of shapes depending on the nature of the input variable and the desired level of granularity. Common shapes include triangular, trapezoidal, Gaussian, and sigmoidal, and each shape is defined by a set of parameters that control its position and shape. Membership functions are a key component of fuzzy logic, and are used to map input values to membership values between 0 and 1.