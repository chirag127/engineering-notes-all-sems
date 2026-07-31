### Implementation of Syntax-Directed Translators

- Syntax-directed translation is a method of compiler implementation where the source language translation is completely driven by the parser.
- A syntax-directed translation scheme is a context-free grammar in which attributes are related to the grammar symbol and semantic actions enclosed within braces ({ }).
- Semantic actions are the subroutines that are called by the parser at the suitable time for translation.
- Semantic actions can perform tasks such as generating intermediate code, building a symbol table, checking types, etc.
- The general approach to syntax-directed translation is to construct a parse tree or syntax tree and compute the values of attributes at the nodes of the tree by visiting them in some order.
- In many cases, translation can be done during parsing without building an explicit tree.
- There are two types of attributes in syntax-directed translation: synthesized and inherited.
- Synthesized attributes are computed from the attributes of the children of a node in the parse tree.
- Inherited attributes are computed from the attributes of the parent and siblings of a node in the parse tree.
- A syntax-directed definition (SDD) is a collection of semantic rules associated with each grammar production.
- A syntax-directed definition is said to be S-attributed if it has only synthesized attributes.
- A syntax-directed definition is said to be L-attributed if it has both synthesized and inherited attributes, but the inherited attributes of a node can be computed from the attributes of its left siblings and parent.
- S-attributed and L-attributed definitions can be implemented during bottom-up or top-down parsing.
- A syntax-directed translation scheme is said to be postfix if the semantic actions are placed at the end of the production.
- A postfix translation scheme can be implemented using a parser stack that stores the attributes of the grammar symbols.
- The parser stack is manipulated by the semantic actions using the following operations:
  - push(x): push the value x onto the stack
  - pop(): pop the top value from the stack and return it
  - top(): return the top value from the stack without popping it
  - assign(i, x): assign the value x to the ith element from the top of the stack
  - access(i): return the value of the ith element from the top of the stack
- An example of a postfix translation scheme for arithmetic expressions is given below:

```
E -> E + T {push('+')}
E -> E - T {push('-')}
E -> T
T -> T * F {push('*')}
T -> T / F {push('/')}
T -> F
F -> (E) {pop()}
F -> digit {push(digit.val)}
```

- The semantic actions generate a postfix notation of the expression, which can be used as an intermediate code.
- For example, the expression `2 * (3 + 4)` is translated to `2 3 4 + *` by the following steps:

```
E -> T -> F -> digit {push(2)}
E -> T -> T * F {push('*')}
E -> T -> T * F -> (E) {pop()}
E -> T -> T * F -> (E -> E + T) {push('+')}
E -> T -> T * F -> (E -> E + T -> T -> F -> digit) {push(3)}
E -> T -> T * F -> (E -> E + T -> T -> F -> digit) {pop()}
E -> T -> T * F -> (E -> E + T -> T -> F) {pop()}
E -> T -> T * F -> (E -> E + T -> F -> digit) {push(4)}
E -> T -> T * F -> (E -> E + T -> F -> digit) {pop()}
E -> T -> T * F -> (E -> E + T -> F) {pop()}
E -> T -> T * F -> (E -> E + T) {pop()}
E -> T -> T * F -> (E) {pop()}
E -> T -> T * F {pop()}
E -> T {pop()}
E
```

- The parser stack after each step is shown below:

```
Step | Stack
-----|------
1    | 2
2    | 2 *
3    | 2
4    |

```
