# Unit 4 - Fuzzy Logic –II (Fuzzy Membership, Rules)

- Fuzzy logic is a form of many-valued logic that deals with the concept of partial truth, where the truth value of variables may be any real number between 0 and 1, instead of just 0 or 1 as in classical logic.
- Fuzzy logic is implemented using fuzzy sets, which are sets that have a degree of membership for each element, rather than a crisp membership of either 0 or 1 as in classical sets.
- The degree of membership of an element in a fuzzy set is determined by a membership function, which is a mapping from an input value to a membership degree between 0 and 1, where 0 represents non-membership and 1 represents full membership .
- Membership functions can have different shapes, such as triangular, trapezoidal, Gaussian, sigmoid, etc., depending on the nature of the input variable and the desired output.
- Fuzzy logic is also implemented using fuzzy rules, which are if-then statements that express the relationship between input variables and output variables in a fuzzy way .
- Fuzzy rules have the form: IF x is A AND y is B THEN z is C, where x, y, and z are input or output variables, and A, B, and C are fuzzy sets defined by membership functions.
- Fuzzy rules can be combined using logical operators such as AND, OR, and NOT, which are also defined by membership functions.
- Fuzzy rules can be evaluated using different methods, such as the Mamdani method, the Sugeno method, the Tsukamoto method, etc., depending on the type of membership functions and the desired output.
- The output of a fuzzy rule is a fuzzy set, which can be converted to a crisp value using a defuzzification method, such as the centroid method, the maximum method, the mean of maxima method, etc.