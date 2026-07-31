### Basic concepts of fuzzy logic

Fuzzy logic is a mathematical method for representing and dealing with vagueness and uncertainty in decision-making. It is based on the idea that some statements or propositions can have a degree of truth or membership that is not just binary (true or false), but can be any real number between 0 and 1. For example, the statement "It is cold today" can have different degrees of truth depending on the context and the person who makes it.

The main components of fuzzy logic are:

- **Membership function**: A function that assigns a degree of membership to each input value in a certain set or category. The membership function can have different shapes, such as triangular, trapezoidal, Gaussian, etc. The membership function is usually denoted by $\mu_A(x)$, where $A$ is the set or category and $x$ is the input value. For example, the membership function for the category "cold" can be defined as:

$$
\mu_{cold}(x) = \begin{cases}
0, & \text{if } x > 20 \\
\frac{20-x}{10}, & \text{if } 10 \leq x \leq 20 \\
1, & \text{if } x < 10
\end{cases}
$$

This means that if the temperature is above 20 degrees Celsius, it is not cold at all (membership degree 0); if the temperature is between 10 and 20 degrees Celsius, it is somewhat cold (membership degree between 0 and 1); and if the temperature is below 10 degrees Celsius, it is very cold (membership degree 1).

- **Fuzzy set**: A set that is defined by a membership function. A fuzzy set can be seen as a generalization of a crisp set, which is a set that has only two membership degrees: 0 or 1. A fuzzy set can be represented by a list of pairs of input values and membership degrees, or by a graphical plot of the membership function. For example, the fuzzy set "cold" can be represented by:

$$
cold = \{(x, \mu_{cold}(x)) | x \in \mathbb{R}\}
$$

or by the following plot:

![cold](https://i.imgur.com/0z0QZ0o.png)

- **Fuzzy rule**: A rule that expresses a logical relationship between fuzzy sets or propositions. A fuzzy rule can have the form of an if-then statement, such as "If the temperature is cold, then turn on the heater". A fuzzy rule can also have multiple antecedents (conditions) and consequents (actions) connected by logical operators, such as "and", "or", "not". For example, a fuzzy rule for controlling the speed of a car can be:

$$
\text{If the road is slippery or the visibility is low, then reduce the speed.}
$$

- **Fuzzy inference**: A process of deriving a conclusion or an output from a set of fuzzy rules and input values. Fuzzy inference can be done using different methods, such as Mamdani, Sugeno, or Tsukamoto. The general steps of fuzzy inference are:

  - **Fuzzification**: Converting the input values into fuzzy sets using the membership functions.
  - **Rule evaluation**: Applying the fuzzy rules to the fuzzy sets and obtaining the fuzzy sets for the consequents.
  - **Aggregation**: Combining the fuzzy sets for the consequents into a single fuzzy set for the output.
  - **Defuzzification**: Converting the fuzzy set for the output into a crisp value using a defuzzification method, such as centroid, maximum, or mean.

For example, suppose we have the following fuzzy sets and rules for controlling the speed of a car:

- Fuzzy sets for the road condition:

$$
\begin{align*}
slippery &= \{(x, \mu_{slippery}(x)) | x \in [0, 1]\} \\
normal &= \{(x, \mu_{normal}(x)) | x \in [0, 1]\} \\
dry &= \{(x, \mu_{dry}(x)) | x \in [0, 1]\}
\end{align*}
$$

where the membership functions are defined as:

$$
\begin{align*}
\mu_{slippery}(x) &= \begin{cases}
1, & \text{if } x \leq 0.2 \\
\frac{0