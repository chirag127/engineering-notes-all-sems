# Fuzzyfication and Defuzzification

- Fuzzyfication and defuzzification are two important steps in fuzzy logic systems, where the input and output variables are mapped from crisp values to fuzzy values and vice versa.
- Fuzzyfication is the process of converting a crisp quantity (such as temperature, speed, distance, etc.) into a fuzzy quantity (such as cold, fast, far, etc.) by assigning a degree of membership to each value in the domain of the variable .
- Defuzzification is the inverse process of fuzzyfication, where the fuzzy output of the fuzzy inference engine is converted into a crisp value (such as 25°C, 60 km/h, 10 m, etc.) so that it can be used in the controller or the application .
- Fuzzyfication and defuzzification are essential for fuzzy logic systems because they allow the system to handle uncertainty and imprecision in the input and output data, and to produce meaningful and actionable results .

## Fuzzyfication

- Fuzzyfication can be done in different ways, depending on the type and nature of the input variable and the fuzzy sets that are defined on its domain.
- One common method of fuzzyfication is to use a membership function, which is a function that assigns a degree of membership (between 0 and 1) to each value in the domain of the variable, based on how well it belongs to a fuzzy set.
- For example, if the input variable is temperature and the fuzzy sets are cold, warm, and hot, then a possible membership function for the cold set is:

![cold](https://codecrucks.com/wp-content/uploads/2021/08/fuzzification-1.png)

- This membership function assigns a degree of membership of 1 to any temperature below 10°C, a degree of membership of 0 to any temperature above 20°C, and a linearly decreasing degree of membership to any temperature between 10°C and 20°C.
- Similarly, membership functions can be defined for the warm and hot sets, and the input temperature can be fuzzyfied by finding its degree of membership in each set.
- Another method of fuzzyfication is to use a fuzzy relation, which is a relation that assigns a degree of membership (between 0 and 1) to each pair of values in the domain and range of the variable, based on how well they are related by a fuzzy concept.
- For example, if the input variable is speed and the fuzzy concept is fast, then a possible fuzzy relation for the fast concept is:

![fast](https://codecrucks.com/wp-content/uploads/2021/08/fuzzification-2.png)

- This fuzzy relation assigns a degree of membership of 1 to any pair of speed and fastness that are equal, a degree of membership of 0 to any pair of speed and fastness that are opposite, and a non-linearly decreasing degree of membership to any pair of speed and fastness that are different.
- The input speed can be fuzzyfied by finding its degree of membership in each level of fastness (slow, medium, fast, very fast, etc.).

## Defuzzification

- Defuzzification can also be done in different ways, depending on the type and nature of the output variable and the fuzzy sets that are defined on its range.
- One common method of defuzzification is to use a centroid method, which is a method that finds the center of gravity of the fuzzy output and returns the value that corresponds to that point as the crisp output.
- For example, if the output variable is temperature and the fuzzy output is a combination of cold, warm, and hot sets, then the centroid method can be applied as follows:

![centroid](https://codecrucks.com/wp-content/uploads/2021/08/defuzzification-1.png)

- The centroid method calculates the area and the moment of each fuzzy set, and then finds the point where the total moment is equal to half of the total area.
- The crisp output is the value that corresponds to that point, which in this case is 23.75°C.
- Another method of defuzzification is to use a maximum method, which is a method that finds the value that has the maximum degree of membership in the fuzzy output and returns that value as the crisp