# Fuzzy Controller

A fuzzy controller is a type of control system that uses fuzzy logic to handle uncertainty and imprecision in the input and output signals. Fuzzy logic is a mathematical system that analyzes analog input values in terms of logical variables that take on continuous values between 0 and 1, in contrast to classical or digital logic, which operates on discrete values of either 1 or 0 (true or false, respectively) .

## Fuzzy Membership

Fuzzy membership is a concept that assigns a degree of belonging to a logical variable, based on a fuzzy set and a membership function. A fuzzy set is a collection of elements that have varying degrees of membership, rather than a crisp set that has only binary membership (either 0 or 1). A membership function is a curve that defines how each element in the input space is mapped to a membership value between 0 and 1 .

For example, consider the fuzzy set of "hot" temperatures, defined by the membership function shown below:

![hot](https://control.com/wp-content/uploads/2020/07/Hot-Temperature-Membership-Function.png)

The membership function assigns a degree of "hotness" to each temperature value, ranging from 0 to 1. For instance, 20°C has a membership value of 0, meaning it is not hot at all, while 40°C has a membership value of 1, meaning it is fully hot. 30°C has a membership value of 0.5, meaning it is somewhat hot .

## Fuzzy Rules

Fuzzy rules are statements that describe the relationship between the input and output variables of a fuzzy controller, using linguistic terms that are defined by fuzzy sets and membership functions. Fuzzy rules have the general form of "IF-THEN" statements, where the IF part is the antecedent or premise, and the THEN part is the consequent or conclusion .

For example, consider a fuzzy controller that regulates the speed of a fan based on the temperature and humidity of the room. The input variables are temperature and humidity, and the output variable is fan speed. The linguistic terms for each variable are defined by fuzzy sets and membership functions, as shown below:

![temp](https://control.com/wp-content/uploads/2020/07/Temperature-Membership-Functions.png)

![hum](https://control.com/wp-content/uploads/2020/07/Humidity-Membership-Functions.png)

![fan](https://control.com/wp-content/uploads/2020/07/Fan-Speed-Membership-Functions.png)

A possible fuzzy rule for this controller is:

IF temperature is high AND humidity is low THEN fan speed is medium

This rule means that if the temperature and humidity values have high and low membership values, respectively, in their corresponding fuzzy sets, then the fan speed value should have a medium membership value in its fuzzy set .

## Fuzzy Controller Design

A fuzzy controller consists of three main stages: fuzzification, inference, and defuzzification .

- Fuzzification: This stage converts the crisp input values into fuzzy values, using the membership functions of the input variables. The output of this stage is a set of fuzzy values that represent the degree of membership of each input value in each fuzzy set.

- Inference: This stage applies the fuzzy rules to the fuzzy input values, using a fuzzy logic operator (such as AND, OR, or NOT) to combine the antecedents and determine the firing strength of each rule. The output of this stage is a set of fuzzy values that represent the degree of membership of each output value in each fuzzy set, based on the fired rules.

- Defuzzification: This stage converts the fuzzy output values into a crisp output value, using a defuzzification method (such as centroid, maxima, or weighted average) to aggregate the fuzzy values and find the best representative value. The output of this stage is a single crisp value that is sent to the actuator or the plant.

![fuzzy](https://control.com/wp-content/uploads/2020/07/Fuzzy-Logic-Controller-Block-Diagram.png)

## Fuzzy Controller Advantages and Applications

Fuzzy controllers have several advantages over conventional controllers, such as:

- They can handle uncertainty and imprecision in the input and output signals, which are common in real-world systems.
- They can incorporate human knowledge and experience into the control system, using linguistic terms and fuzzy rules that are easy to understand and modify.
- They can deal with non-linearity and complexity in the system, without requiring