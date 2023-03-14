The following is a detailed ASCII diagram for Cause Effect Graphing Technique for the notes of the Unit 2 - Functional Testing in the subject of Software Testing.

### Cause Effect Graphing Technique

A cause effect graph is a graphical representation of the relationship between the input conditions (causes) and the output conditions (effects) of a system or a specification. It is used to derive test cases that cover all possible combinations of input conditions and their effects on the output. The graph consists of nodes, edges and logical operators.

The nodes represent the causes and effects, which are labeled with C and E respectively, followed by a number. The edges represent the connections between the causes and effects, which are labeled with the logical operators AND, OR and NOT. The logical operators indicate how the causes and effects are related. For example, C1 AND C2 means that both C1 and C2 must be true for the effect to occur. C1 OR C2 means that either C1 or C2 must be true for the effect to occur. NOT C1 means that C1 must be false for the effect to occur.

The graph also includes constraints, which are special conditions that limit the possible combinations of causes and effects. The constraints are labeled with E, I, O and R, followed by a number. The constraints are represented by dashed lines between the nodes. The constraints have the following meanings:

- E-constraint: Exclusive constraint. It means that only one of the connected causes can be true at a time. For example, E1 between C1 and C2 means that C1 and C2 cannot be true simultaneously.
- I-constraint: Inclusive constraint. It means that at least one of the connected causes must be true at a time. For example, I1 between C1, C2 and C3 means that C1, C2 and C3 cannot be false simultaneously.
- O-constraint: One and only one constraint. It means that exactly one of the connected causes must be true at a time. For example, O1 between C1 and C2 means that either C1 or C2 must be true, but not both.
- R-constraint: Requires constraint. It means that one cause requires another cause to be true. For example, R1 between C1 and C2 means that C1 can only be true if C2 is true.

The diagram below shows an example of a cause effect graph for a system that validates a password. The causes are:

- C1: Password is blank
- C2: Password is less than 8 characters
- C3: Password contains only letters
- C4: Password contains only numbers
- C5: Password contains special characters

The effects are:

- E1: Password is accepted
- E2: Password is rejected
- E3: Error message is displayed

The constraints are:

- E1: Between C1 and C2. It means that the password cannot be blank and less than 8 characters at the same time.
- E2: Between C3 and C4. It means that the password cannot contain only letters and only numbers at the same time.
- R1: Between C5 and E1. It means that the password can only be accepted if it contains special characters.

The cause effect graph is shown below:

```
    C1
    |
    |  E1
    | /
    |/
    E-constraint
    /\
    | \
    |  C2
    |
    |  E2
    | /
    |/
    E1----R1----C5
    |\
    | \
    |  E3
    | /
    |/
    E-constraint
    /\
    | \
    |  C3
    |
    |  E2
    | /
    |/
    E-constraint
    /\
    | \
    |  C4
```

The cause effect graph can be converted into a decision table, which shows the values of the causes and effects for each test case. The decision table for the above graph is shown below:

| C1 | C2 | C3 | C4 | C5 | E1 | E2 | E3 |
|----|----|----|----|----|----|----|----|
| T  | F  | F  | F  | F  | F  | T  | T  |
| F  | T  | F  | F  | F  | F  | T  | T  |
| F  | F  | T  | F