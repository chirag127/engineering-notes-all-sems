Syntactic analysis is the process of checking if the source code follows the grammatical rules of the programming language. It is typically the second stage of the compilation process, following lexical analysis. Syntactic analysis can also be applied to natural language processing, where it is used to draw the dictionary meaning of sentences or phrases based on the rules of formal grammar.

A common way to represent the syntactic structure of a sentence or a phrase is to use a tree diagram. A tree diagram consists of nodes and branches that show the hierarchical relationship between the syntactic units, such as words, phrases, and clauses. The root node represents the whole sentence or phrase, and the leaf nodes represent the individual words or tokens. The intermediate nodes represent the syntactic categories, such as noun phrase (NP), verb phrase (VP), adjective phrase (AP), etc. The branches show how the syntactic units are combined to form larger units .

The following diagram illustrates the basic architecture of a syntactic analyzer in compiler design:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Lexical        |     |  Syntax         |     |  Semantic       |
|  Analyzer       |---->|  Analyzer       |---->|  Analyzer       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Source code    |     |  Tokens         |     |  Parse tree     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The lexical analyzer takes the source code as input and produces a sequence of tokens as output. The syntax analyzer takes the tokens as input and produces a parse tree as output. The parse tree represents the syntactic structure of the source code. The semantic analyzer takes the parse tree as input and performs semantic checks, such as type checking, scope checking, etc. The semantic analyzer produces an annotated parse tree as output, which can be used for further stages of compilation.

The following diagram illustrates an example of a syntactic tree for the sentence "The big dog barked loudly" in natural language processing:

```
              S
             / \
            /   \
           /     \
          NP      VP
         / \     /  \
        /   \   /    \
       /     \ /      \
      DT     AP       ADVP
     /      / \       /  \
    /      /   \     /    \
   /      /     \   /      \
  /      /       \ /        \
The    JJ        N          RB
      /         /          /
     /         /          /
    /         /          /
   /         /          /
 big       dog       loudly
```

The sentence (S) consists of a noun phrase (NP) and a verb phrase (VP). The noun phrase consists of a determiner (DT) and an adjective phrase (AP). The adjective phrase consists of an adjective (JJ) and a noun (N). The verb phrase consists of a verb (V) and an adverb phrase (ADVP). The adverb phrase consists of an adverb (RB). The leaf nodes represent the individual words or tokens, and the intermediate nodes represent the syntactic categories  .