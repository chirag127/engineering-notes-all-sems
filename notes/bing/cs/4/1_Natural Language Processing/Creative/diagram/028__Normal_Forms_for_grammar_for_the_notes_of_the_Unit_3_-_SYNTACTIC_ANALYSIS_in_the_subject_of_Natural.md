Normal Forms for grammar are ways of simplifying the rules of a context-free grammar to make it easier to parse or analyze. There are two common normal forms: Chomsky Normal Form (CNF) and Greibach Normal Form (GNF).

A grammar is in CNF if all its rules are of the form A -> BC or A -> a, where A, B, and C are nonterminals and a is a terminal. A grammar is in GNF if all its rules are of the form A -> aB1B2...Bn, where A and Bi are nonterminals and a is a terminal.

The following diagram illustrates the basic structure of a grammar in CNF and GNF using ASCII art:

```
CNF:                GNF:

  A                  A
 / \                / \
B   C              a   B1
|   |                  / \
a   b                 b   B2
                         / \
                        c   B3
                         / \
                        d   B4
                         / \
                        e   B5
                         / \
                        f   B6
                         / \
                        g   B7
                         / \
                        h   B8
                         / \
                        i   B9
                         / \
                        j   B10
                         / \
                        k   B11
                         / \
                        l   B12
                         / \
                        m   B13
                         / \
                        n   B14
                         / \
                        o   B15
                         / \
                        p   B16
                         / \
                        q   B17
                         / \
                        r   B18
                         / \
                        s   B19
                         / \
                        t   B20
                         / \
                        u   B21
                         / \
                        v   B22
                         / \
                        w   B23
                         / \
                        x   B24
                         / \
                        y   B25
                         / \
                        z   B26
                         / \
                        A   B27
                         / \
                        B   C
```