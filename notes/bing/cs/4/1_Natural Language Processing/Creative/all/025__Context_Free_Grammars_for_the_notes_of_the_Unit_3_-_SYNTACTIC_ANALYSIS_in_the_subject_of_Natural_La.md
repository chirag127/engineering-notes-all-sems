### Context Free Grammars for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

- A context-free grammar (CFG) is a list of rules that define the set of all well-formed sentences in a language.
- Each rule has a left-hand side, which identifies a syntactic category, and a right-hand side, which defines its alternative component parts, reading from left to right.
- A syntactic category is a label for a group of words or phrases that share some common properties, such as noun, verb, adjective, etc.
- A context-free grammar is called so because the rules can be applied regardless of the surrounding context of the words or phrases.
- A context-free grammar can be represented by a tuple (N, T, P, S), where:
  - N is a set of non-terminal symbols, which are the syntactic categories that can be further expanded by the rules.
  - T is a set of terminal symbols, which are the words or tokens that cannot be further expanded by the rules.
  - P is a set of production rules, which specify how a non-terminal symbol can be rewritten as a sequence of terminal or non-terminal symbols.
  - S is a special non-terminal symbol, called the start symbol, which represents the whole sentence or program.
- For example, a simple context-free grammar for a subset of English sentences can be defined as follows:
  - N = {S, NP, VP, Det, N, V, PP, P}
  - T = {a, the, dog, cat, mouse, chased, ate, on, under, table, sofa}
  - P = {S -> NP VP, NP -> Det N, NP -> NP PP, VP -> V NP, VP -> VP PP, Det -> a | the, N -> dog | cat | mouse | table | sofa, V -> chased | ate, PP -> P NP, P -> on | under}
  - S = S
- A context-free grammar can be used to generate or parse sentences or programs in a language.
- To generate a sentence or program, we start with the start symbol and apply the rules randomly until we get a sequence of terminal symbols.
- To parse a sentence or program, we start with the sequence of terminal symbols and try to find a sequence of rule applications that can produce it from the start symbol.
- A context-free grammar can be represented by a parse tree, which is a graphical representation of the derivation of a sentence or program from the start symbol.
- A parse tree shows the hierarchical structure of the sentence or program, and the labels of the nodes indicate the syntactic categories of the words or phrases.
- For example, the parse tree for the sentence "the dog chased the cat on the sofa" using the grammar above is:

```
              S
             / \
            /   \
           /     \
          NP      VP
         / \     /  \
        /   \   /    \
       /     \ /      \
      Det     N        PP
      |       |       /  \
      |       |      /    \
      |       |     /      \
      the    dog    P       NP
                  / \      / \
                 /   \    /   \
                /     \  /     \
               on     Det      N
                      |        |
                      |        |
                      the     cat
```

- A context-free grammar can be used to model the constituent structure of natural language, which is the way words and phrases are grouped together to form larger units of meaning.
- A constituent is a word or a group of words that functions as a single unit within a hierarchical structure.
- For example, in the sentence "the dog chased the cat on the sofa", the noun phrase "the dog" is a constituent that acts as the subject of the verb phrase "chased the cat on the sofa", which is another constituent that acts as the predicate of the sentence.
- A context-free grammar can capture some of the syntactic regularities and variations of natural language, such as word order, agreement, subordination, coordination, etc.
- For example, the grammar above can generate sentences with different word orders, such as "the cat chased the dog on the sofa" or "on the sofa, the dog chased the cat", by applying different rules.