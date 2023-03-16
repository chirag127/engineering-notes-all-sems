# Fuzzy to Crisp Conversion

- Fuzzy to crisp conversion, also known as defuzzification, is the process of transforming a fuzzy set or a fuzzy output into a single crisp value or a crisp set.
- Fuzzy to crisp conversion is often needed in fuzzy logic applications, such as fuzzy control systems, fuzzy decision making, fuzzy pattern recognition, etc., where a precise output or action is required based on fuzzy inputs or rules.
- There are many methods for fuzzy to crisp conversion, each with its own advantages and disadvantages. Some of the common methods are:

  - Maxima methods: These methods select the crisp value(s) that correspond to the maximum degree(s) of membership in the fuzzy set or output. Examples of maxima methods are:
    - Mean of Maxima (MoM): This method calculates the average of all the crisp values that have the maximum degree of membership in the fuzzy set or output.
    - First of Maxima (FoM): This method selects the smallest crisp value that has the maximum degree of membership in the fuzzy set or output.
    - Last of Maxima (LoM): This method selects the largest crisp value that has the maximum degree of membership in the fuzzy set or output.
    - Decision Expected Element (DEE): This method selects the crisp value that has the maximum degree of membership in the fuzzy set or output, and if there are more than one such values, it selects the one that is closest to the expected value of the fuzzy set or output.
  - Center methods: These methods select the crisp value that represents the center or balance point of the fuzzy set or output. Examples of center methods are:
    - Center of Gravity (CoG): This method calculates the weighted average of all the crisp values in the fuzzy set or output, where the weights are the degrees of membership.
    - Center of Sums (CoS): This method calculates the ratio of the sum of all the crisp values in the fuzzy set or output to the sum of all the degrees of membership.
    - Center of Area (CoA): This method calculates the crisp value that divides the area under the membership function of the fuzzy set or output into two equal parts.
    - Bisector of Area (BoA): This method calculates the crisp value that divides the area under the membership function of the fuzzy set or output into two equal parts, and if there are more than one such values, it selects the one that is closest to the center of gravity of the fuzzy set or output.
  - Lambda-cut methods: These methods select the crisp value(s) that belong to a subset of the fuzzy set or output that has a certain degree of membership or higher. Examples of lambda-cut methods are:
    - Lambda-max method: This method selects the crisp value(s) that belong to the subset of the fuzzy set or output that has the maximum degree of membership.
    - Lambda-mean method: This method selects the crisp value(s) that belong to the subset of the fuzzy set or output that has the average degree of membership.
    - Lambda-med method: This method selects the crisp value(s) that belong to the subset of the fuzzy set or output that has the median degree of membership.