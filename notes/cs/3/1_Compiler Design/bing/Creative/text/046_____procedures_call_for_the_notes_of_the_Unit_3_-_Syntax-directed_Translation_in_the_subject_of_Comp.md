Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design.

### Syntax-directed Translation
- Syntax-directed translation is a method of translating a source program into a target program using the syntactic structure of the source program.
- Syntax-directed translation can be performed at compile time or run time, depending on when the syntactic structure of the source program is available.
- Syntax-directed translation can be implemented using two techniques: syntax-directed definitions and translation schemes.

### Syntax-directed Definitions
- A syntax-directed definition (SDD) is a way of specifying the translation of a context-free grammar by attaching semantic rules to the grammar productions.
- A semantic rule is a function that computes some attribute values from the attribute values of the symbols in the production.
- An attribute is a property of a grammar symbol or a grammar rule that can hold a value.
- There are two types of attributes: synthesized attributes and inherited attributes.
- A synthesized attribute is an attribute of a nonterminal that is computed from the attribute values of its children in the parse tree.
- An inherited attribute is an attribute of a nonterminal that is computed from the attribute values of its parent and siblings in the parse tree.
- A syntax-directed definition is said to be S-attributed if it has only synthesized attributes, and L-attributed if it has both synthesized and inherited attributes, but the inherited attributes can be evaluated in a single left-to-right traversal of the parse tree.
- An example of an SDD for arithmetic expressions is:

```
E -> E1 + T { E.val = E1.val + T.val }
E -> T { E.val = T.val }
T -> T1 * F { T.val = T1.val * F.val }
T -> F { T.val = F.val }
F -> ( E ) { F.val = E.val }
F -> num { F.val = num.val }
```

- An example of an LDD for type checking is:

```
S -> id : T { id.type = T.type }
T -> integer { T.type = integer }
T -> T1 [ num ] { T.type = array(num.val, T1.type) }
```

### Translation Schemes
- A translation scheme is a way of specifying the translation of a context-free grammar by embedding semantic actions in the grammar productions.
- A semantic action is a piece of code that is executed when the corresponding production is recognized by the parser.
- A semantic action can access and modify the attribute values of the symbols in the production, as well as perform other operations such as generating intermediate code, printing output, or reporting errors.
- A translation scheme can be converted into an SDD by replacing each semantic action with an attribute and a semantic rule that assigns the value of the attribute to the result of the semantic action.
- An example of a translation scheme for arithmetic expressions is:

```
E -> E1 + T { print('+') }
E -> T
T -> T1 * F { print('*') }
T -> F
F -> ( E ) 
F -> num { print(num.val) }
```

- An example of a translation scheme for type checking is:

```
S -> id : T { if id.type != T.type then error() }
T -> integer
T -> T1 [ num ] { if num.val <= 0 then error() }
```