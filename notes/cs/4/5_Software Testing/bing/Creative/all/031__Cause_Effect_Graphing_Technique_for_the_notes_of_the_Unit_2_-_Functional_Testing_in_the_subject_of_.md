### Cause Effect Graphing Technique for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

- Cause Effect Graphing Technique is a black box testing technique that graphically illustrates the relationship between a given outcome (effect) and all the factors (causes) that influence the outcome   .
- It is also known as Ishikawa diagram or fish bone diagram because of the way it looks, invented by Kaoru Ishikawa .
- It is based on a collection of requirements and used to determine minimum possible test cases that can cover a maximum test area of the software.
- The main advantage of cause-effect graph testing is, it reduces the time of test execution and cost.
- The main disadvantage of cause-effect graph testing is, it is difficult to work with large and complex specifications, and it does not consider the dependencies among causes and effects.

#### Steps to apply Cause Effect Graphing Technique :

1. Divide the specification into small workable pieces and identify the causes (distinct input conditions) and effects (output conditions) in each piece.
2. Transform the specification into a cause-effect graph by linking the causes and effects using Boolean expressions and adding constraints if possible.
3. Convert the cause-effect graph into a limited entry decision table by assigning values to the causes and effects and applying the Boolean logic and constraints.
4. Derive test cases from each column of the decision table by providing test inputs and expected outputs.

#### Symbols used in Cause Effect Graphing Technique :

- A cause or an effect is represented by a circle with a label inside.
- An identity function is represented by a line connecting a cause and an effect, meaning that the effect is the same as the cause.
- A NOT function is represented by a line with a slash connecting a cause and an effect, meaning that the effect is the opposite of the cause.
- An OR function is represented by a line with a plus sign connecting multiple causes and an effect, meaning that the effect is true if any of the causes is true.
- An AND function is represented by a line with a dot connecting multiple causes and an effect, meaning that the effect is true if all of the causes are true.
- An exclusive constraint (E-constraint) is represented by a line with an E connecting two causes, meaning that only one of the causes can be true at a time.
- An inclusive constraint (I-constraint) is represented by a line with an I connecting multiple causes, meaning that at least one of the causes must be true.
- A one and only one constraint (O-constraint) is represented by a line with an O connecting two causes, meaning that exactly one of the causes must be true.
- A requires constraint (R-constraint) is represented by a line with an R connecting two causes, meaning that the first cause requires the second cause to be true.
- A mask constraint (M-constraint) is represented by a line with an M connecting two effects, meaning that the first effect masks the second effect.

#### Example of Cause Effect Graphing Technique :

Consider the following specification for a triangle problem:

- A valid triangle can be formed if and only if the sum of any two sides is greater than the third side.
- If all the three sides are equal, then the triangle is equilateral.
- If only two sides are equal, then the triangle is isosceles.
- If no sides are equal, then the triangle is scalene.

The causes and effects for this specification are:

- C1: Side x is less than the sum of y and z
- C2: Side y is less than the sum of x and z
- C3: Side z is less than the sum of x and y
- C4: Side x is equal to side y
- C5: Side y is equal to side z
- C6: Side z is equal to side x
- E1: Valid triangle
- E2: Equilateral triangle
- E3: Isosceles triangle
- E4: Scalene triangle

The cause-effect graph for this specification is:

```
    C1  C2  C3
     \  |  /
      \ | /
       \|/
        +
        |
        E1
        |
        |
        +-----------------+
        |                 |
        |                 |
        |                 |
        |                 |