# Fuzzy If-Then Rules

- Fuzzy if-then rules are expressions of the form "If x is A then y is B", where x and y are variables, and A and B are linguistic values defined by fuzzy sets on the domains of x and y, respectively.
- Fuzzy if-then rules are used to represent fuzzy knowledge or fuzzy logic, which is a form of reasoning that deals with imprecise or vague information.
- Fuzzy if-then rules can be interpreted as fuzzy relations or fuzzy implications, which are subsets of the Cartesian product of the domains of x and y, with a membership function that assigns a degree of truth to each pair of values .
- Fuzzy if-then rules can be classified into two types: Mamdani-type and Takagi-Sugeno-type.
  - Mamdani-type rules have fuzzy sets as consequents, and are used for fuzzy control or fuzzy classification problems. For example, "If temperature is high then fan speed is fast".
  - Takagi-Sugeno-type rules have linear functions or constants as consequents, and are used for fuzzy modeling or fuzzy approximation problems. For example, "If temperature is high then fan speed is 0.8 * temperature + 10".
- Fuzzy if-then rules can be combined to form a fuzzy rule base, which is a collection of rules that cover the possible situations or scenarios of a problem domain. A fuzzy rule base can be used to perform fuzzy inference, which is the process of deriving a fuzzy output from a fuzzy input, using the rules and a set of inference methods  .
- Fuzzy inference methods can be divided into two steps: aggregation and defuzzification .
  - Aggregation is the process of combining the outputs of all the rules that are activated by the input, using a fuzzy operator such as max, min, or sum. The result is a fuzzy set that represents the overall output.
  - Defuzzification is the process of converting the fuzzy output into a crisp value, using a technique such as centroid, mean of maxima, or height. The result is a single value that represents the best compromise among the outputs of the rules.