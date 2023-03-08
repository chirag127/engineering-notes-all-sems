### Constructing Canonical LR Parsing Tables

In the field of compiler design, parsing is a fundamental process that involves analyzing a sequence of tokens to determine their grammatical structure. One of the most commonly used parsing techniques is the LR parsing technique, which involves constructing a parsing table that can be used to efficiently parse input strings. In this unit, we will focus on the construction of Canonical LR Parsing Tables, which is an extension of LR parsing.

#### What is Canonical LR Parsing?

Canonical LR Parsing is a parsing technique that is based on the LR parsing technique. It is used to parse programming languages that have a context-free grammar. In this technique, a parsing table is constructed using a set of LR(0) items, which are the basic building blocks of the LR parsing technique. The Canonical LR Parsing technique is more powerful than the LR parsing technique as it can handle more complex grammars and can parse a wider variety of programming languages.

#### Constructing Canonical LR Parsing Tables

The process of constructing a Canonical LR Parsing Table involves the following steps:

1. Constructing the LR(0) item sets: In this step, we start with the initial state of the grammar and generate a set of LR(0) items. These items represent the possible configurations of the parser at a particular point in time. The LR(0) item sets are generated using a closure operation.

2. Computing the LR(0) transitions: In this step, we compute the transitions between the LR(0) item sets. These transitions are generated using a goto operation.

3. Computing the lookahead sets: In this step, we compute the lookahead sets for each LR(0) item. The lookahead sets represent the set of terminals that can follow the non-terminal in a particular item.

4. Constructing the Canonical LR Parsing Table: In this step, we use the LR(0) item sets, transitions, and lookahead sets to construct the Canonical LR Parsing Table. The table contains the actions that the parser should take when it encounters a particular terminal or non-terminal.

#### Advantages of Canonical LR Parsing

- It can handle more complex grammars than the LR parsing technique.
- It can parse a wider variety of programming languages.
- It is more efficient than other parsing techniques.

#### Disadvantages of Canonical LR Parsing

- It can be difficult to implement as it requires a lot of computational power.
- It can be time-consuming to construct the parsing table.

#### Example

Consider the following grammar:

```
S → E
E → E + T
E → T
T → T * F
T → F
F → ( E )
F → id
```

The LR(0) item sets for this grammar are:

```
I0: S → .E
    E → .E + T
    E → .T
    T → .T * F
    T → .F
    F → .( E )
    F → .id

I1: S → E.

I2: E → E. + T
    T → .T * F
    T → .F
    F → .( E )
    F → .id

I3: E → T.

I4: T → T. * F
    F → .( E )
    F → .id

I5: T → F.

I6: F → (.E)
    E → .E + T
    E → .T
    T → .T * F
    T → .F
    F → .( E )
    F → .id

I7: F → id.

The Canonical LR Parsing Table for this grammar is:

| State | id | + | * | ( | ) | $ | S | E | T | F |
|-------|----|---|---|---|---|---|---|---|---|---|
| 0     | s6 |   |   | s5|   |   | 1 | 2 | 3 | 4 |
| 1     |   |   |   |   |   | acc|   |   |   |   |
| 2     |   | s7|   |   |   | r3|   |   |   |   |
| 3     |   | r5| s8|   | r5| r5|   |   |   |   |
| 4     |   | r4| r4|   | r4| r4|   |   |   |   |
| 5     | s6 |   |   | s5|   |   |   | 9 | 3 | 4 |
| 6     |   | r7| r7|   | r7| r7|   |   |   |   |
| 7     | s6 |   |   | s5|   |   |   |   | 10| 4 |
| 8