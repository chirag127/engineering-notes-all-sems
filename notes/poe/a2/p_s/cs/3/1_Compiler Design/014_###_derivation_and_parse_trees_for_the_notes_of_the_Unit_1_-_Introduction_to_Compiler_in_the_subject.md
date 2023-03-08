 Here is the content in markdown format for the topic - ### Derivation and Parse Trees for the notes of Unit 1 - Introduction to Compiler in the subject of Compiler Design:

### Derivation Trees
- Derivation trees show the derivation of a string from the start symbol of a grammar.
- They are a visual way to show the application of productions to derive a string.
- Each node in the tree is a nonterminal and has child nodes that are the rhs of the production used.
- The leaves are the terminals (tokens) of the input string.
- Path from root to leaf shows the sequence of productions used to derive the input string.

For example, consider grammar:
S → aSb | ab

Derivation tree for input string 'aab':

S
├── a
└── Sb
    ├── a
    └── b

Advantages:
- Clearly show the sequence of productions used.
- Can detect left recursion and left factoring.

Disadvantages:
- Can be exponential in size.

### Parse Trees
- Parse trees are a condensed representation of a derivation tree.
- They merge all repeated instances of nonterminals.
- The path from root to a leaf node spells out the sequence of reductions.
- Every node is labeled by either a terminal or nonterminal.
- The children of a nonterminal node are the components in the right-hand side of the production for that nonterminal.

For example, parse tree for grammar:
E → E + T | T
T → T * F | F
F → (E) | id

and input string 'id + id * id':

E
├── T
│   ├── F
│   │   └── id
│   └── *
│       └── F
│           └── id
└── +
    └── T
        ├── F
        │   └── id
        └── *
            └── F
                └── id

Advantages:
- Condensed representation compared to derivation trees.
- Clearly show the structure of the input string.