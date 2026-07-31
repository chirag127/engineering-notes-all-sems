# Declarations and Case Statements

## Declarations

- Declarations are used to specify the types and names of variables, constants, functions, and other entities in a program.
- Declarations can be syntax-directed translated by augmenting the grammar that defines the syntax of declarations with semantic rules that associate attributes with the nonterminals and terminals of the grammar.
- Attributes can be used to store information such as the name, type, size, and location of a declared entity.
- A common technique for syntax-directed translation of declarations is to use a symbol table, which is a data structure that maps names to their attributes.
- An example of a grammar that defines declarations and simple expressions in a Pascal-like syntax is:

```
P -> DS
D -> var V; D | ε
S -> V := E; S | ε
V -> x | y | z
E -> V | E + E | E * E | (E)
```

- An example of a syntax-directed translation scheme that associates attributes `name` and `dl` (declaration list) with the nonterminals `P`, `D`, and `V`, and computes the size and location of each variable is:

```
P -> DS { print P.dl }
D -> var V; D1 { V.entry = newentry(V.name, integer);
                 D.dl = D1.dl || V.entry }
  | ε { D.dl = nil }
S -> V := E; S1 | ε
V -> x { V.name = "x" }
  | y { V.name = "y" }
  | z { V.name = "z" }
E -> V | E1 + E2 | E1 * E2 | (E1)
```

## Case Statements

- Case statements are used to execute different statements based on the value of an expression.
- Case statements can be syntax-directed translated by augmenting the grammar that defines the syntax of case statements with semantic rules that generate intermediate code for each case.
- Intermediate code is a representation of the program that is closer to the target machine language than the source language, but still independent of the target machine details.
- A common technique for syntax-directed translation of case statements is to use labels and jumps, which are intermediate code instructions that specify the location of the next instruction to be executed.
- An example of a grammar that defines case statements in a C-like syntax is:

```
S -> switch E begin L end
L -> C L | ε
C -> case V : S
```

- An example of a syntax-directed translation scheme that generates intermediate code for case statements using labels and jumps is:

```
S -> switch E begin L end { L.next = newlabel();
                             gen("goto", L.next) }
L -> C L1 { L.begin = C.begin;
             L.next = L1.next;
             gen(L.begin, ":") }
  | ε { L.begin = L.next }
C -> case V : S { C.begin = newlabel();
                   gen("if", E.place, "=", V.place, "goto", C.begin);
                   backpatch(S.next, L.begin) }
```