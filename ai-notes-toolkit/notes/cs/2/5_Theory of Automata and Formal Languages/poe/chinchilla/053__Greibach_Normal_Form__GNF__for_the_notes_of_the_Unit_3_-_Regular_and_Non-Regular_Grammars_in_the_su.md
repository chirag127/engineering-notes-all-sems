

### Greibach Normal Form (GNF)

Greibach Normal Form (GNF) is a type of normal form for context-free grammars. It is named after Sheila Greibach, who introduced it in 1974.

#### Definition

A context-free grammar is said to be in Greibach Normal Form if it is of the following form:

- The start symbol appears only on the left-hand side of a production.
- All productions are of the form `A → aα`, where `A` is a nonterminal symbol, `a` is a terminal symbol, and `α` is a string of nonterminal symbols (possibly empty), such that the leftmost symbol of `α` is distinct from `A`.
- There are no ε-productions (productions of the form `A → ε`, where `ε` is the empty string).

#### Conversion

To convert a context-free grammar into Greibach Normal Form, we can follow the following steps:

1. Eliminate ε-productions, unit productions, and useless symbols.
2. Replace all productions of the form `A → αBβ` with `A → aA'`, where `a` is the leftmost terminal symbol in `α`, and `A' → βA' | ε` is a new nonterminal symbol.
3. Replace all nonterminal symbols that have more than one production with new nonterminal symbols.

#### Advantages

There are several advantages to using Greibach Normal Form:

- It is a simpler form than Chomsky Normal Form.
- Parsing algorithms for GNF grammars are more efficient than for arbitrary context-free grammars.
- GNF is useful in the design of compilers, since it allows for efficient parsing and code generation.

#### Example

Consider the following context-free grammar:

```
S → aSb | ε
```

We can convert it into Greibach Normal Form as follows:

1. Eliminate ε-productions:

```
S → aSb | ab
```

2. Eliminate unit productions:

```
S → AB | ab
A → aS
B → b
```

3. Eliminate useless symbols:

```
S → AB
A → aS
B → b
```

4. Replace productions of the form `A → αBβ`:

```
S → AB
A → aA'
A' → BS | ε
B → b
```

Now, the grammar is in Greibach Normal Form.