# Fuzzyfications & Defuzzificataions

- Fuzzyfications and defuzzificataions are two important steps in the fuzzy inference system, which is a method of reasoning with imprecise and uncertain information.
- Fuzzyfications is the process of transforming a crisp set to a fuzzy set or a fuzzy set to a fuzzier set. A crisp set is a set that has clear boundaries and membership values, such as {1, 2, 3, 4, 5}. A fuzzy set is a set that has fuzzy boundaries and membership values, such as {low, medium, high}.
- Defuzzificataions is the process of reducing a fuzzy set into a crisp set or converting a fuzzy member into a crisp member. A crisp member is a member that has a definite value, such as 3. A fuzzy member is a member that has a range of values, such as around 3.
- Fuzzyfications and defuzzificataions are used to handle the input and output of the fuzzy inference system. The input is usually a crisp value that needs to be fuzzified into a fuzzy value, and the output is usually a fuzzy value that needs to be defuzzified into a crisp value.
- There are different methods of fuzzyfications and defuzzificataions, depending on the type and shape of the fuzzy sets and the desired level of precision and accuracy. Some common methods are:
  - Fuzzyfications methods:
    - Singleton fuzzifier: assigns a membership value of 1 to a single crisp value and 0 to all other values.
    - Gaussian fuzzifier: assigns a membership value based on a Gaussian function, which has a bell-shaped curve.
    - Triangular fuzzifier: assigns a membership value based on a triangular function, which has a linear increase and decrease.
    - Trapezoidal fuzzifier: assigns a membership value based on a trapezoidal function, which has a linear increase, a constant value, and a linear decrease.
  - Defuzzificataions methods:
    - Centroid method: calculates the center of gravity of the fuzzy set and returns the crisp value that corresponds to it.
    - Bisector method: calculates the vertical line that divides the fuzzy set into two equal areas and returns the crisp value that corresponds to it.
    - Mean of maxima method: calculates the average of the crisp values that have the maximum membership value in the fuzzy set and returns it.
    - Max criterion method: returns the crisp value that has the maximum membership value in the fuzzy set. If there are more than one, it returns the smallest or the largest one.