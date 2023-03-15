### Parse trees and syntax trees

- Parse trees and syntax trees are data structures that represent the syntactic structure of a source code in compiler design.
- A parse tree is created by a parser, which is a component of a compiler that processes the source code and checks it for syntactic correctness.
- A syntax tree is an abstract or compact representation of a parse tree, which omits some details that are not relevant for translation.
- Parse trees and syntax trees are used for different tasks in compiler design, such as syntax analysis, semantic analysis, intermediate code generation, and code optimization.

#### Parse tree

- A parse tree is a hierarchical structure that shows how a string of tokens is derived from the grammar rules of a language.
- A parse tree has the following properties:
  - The root node is the start symbol of the grammar.
  - The internal nodes are non-terminals of the grammar.
  - The leaf nodes are terminals of the grammar.
  - The order of the children of a node corresponds to the order of the symbols in the right-hand side of the grammar rule.
  - The string of tokens can be obtained by traversing the parse tree in a left-to-right, depth-first order (also called a pre-order traversal).
- A parse tree can be represented graphically or textually. For example, consider the following grammar for arithmetic expressions:

  ```
  E -> E + T | T
  T -> T * F | F
  F -> (E) | id
  ```

  The parse tree for the expression `id + id * id` can be shown as:

  ```
              E
             / \
            E   T
           / \ / \
          T  + T F
         / \  | | |
        F  *  F id id
       / \ | / \
      id id id id
  ```

  or as:

  ```
  (E (E (T (F id)) + (T (T (F id)) * (F id))) )
  ```

- A parse tree can be ambiguous, meaning that there can be more than one way to derive the same string of tokens from the grammar rules. For example, the expression `id + id * id` can also have the following parse tree:

  ```
              E
             / \
            E   T
           / \   \
          E  +    F
         / \     / \
        T  id   id id
       / \
      F  *
     / \
    id id
  ```

  or as:

  ```
  (E (E (T (F id)) + (E (T (F id)) * (F id))) )
  ```

- Ambiguity can cause problems for translation, as different parse trees may have different meanings or semantics. Therefore, a grammar should be designed to avoid ambiguity, or some disambiguation techniques should be applied to resolve the ambiguity.

#### Syntax tree

- A syntax tree is a simplified version of a parse tree, which removes some unnecessary nodes and symbols, and preserves only the essential information for translation.
- A syntax tree has the following properties:
  - The root node is the main operator or construct of the source code.
  - The internal nodes are operators or constructs of the source code.
  - The leaf nodes are operands or identifiers of the source code.
  - The order of the children of a node corresponds to the order of evaluation of the operator or construct.
  - The string of tokens can be obtained by traversing the syntax tree in a left-to-right, depth-first order (also called a pre-order traversal), and inserting parentheses as needed.
- A syntax tree can be represented graphically or textually. For example, the syntax tree for the expression `id + id * id` can be shown as:

  ```
          +
         / \
        id  *
           / \
          id id
  ```

  or as:

  ```
  (+ id (* id id))
  ```

- A syntax tree is unambiguous, meaning that there is only one way to construct the syntax tree for a given string of tokens. For example, the expression `id + id * id` can only have the syntax tree shown above, regardless of the grammar rules.
- A syntax tree can be used for various tasks in compiler design, such as semantic analysis, intermediate code generation, and code optimization. For example, the syntax tree can be annotated with type information, or transformed into a three-address code, or simplified by applying