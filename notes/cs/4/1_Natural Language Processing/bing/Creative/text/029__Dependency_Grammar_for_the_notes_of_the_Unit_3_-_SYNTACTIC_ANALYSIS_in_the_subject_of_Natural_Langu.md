### Dependency Grammar

- Dependency grammar is a descriptive and theoretical tradition in linguistics that can be traced back to antiquity.
- It has long been influential in the European linguistics tradition and has more recently become a mainstream approach to representing syntactic and semantic structure in natural language processing.
- The basic assumption underlying all varieties of dependency grammar is the idea that syntactic structure essentially consists of words linked by binary, asymmetrical relations called dependency relations (or dependencies for short).
- A dependency relation holds between a syntactically subordinate word, called the dependent, and another word on which it depends, called the head.
- This is illustrated in figure 1, which shows a dependency structure for a simple English sentence, where dependency relations are represented by arrows pointing from the head to the dependent.
- Moreover, each arrow has a label, indicating the dependency type. For example, the noun news is a dependent of the verb had with the dependency type subject (SBJ). By contrast, the noun effect is a dependent of type object (OBJ) with the same head verb had.
- One peculiarity of the dependency structure in figure 1 is that we have inserted an artificial word root before the first word of the sentence. This is a mere technicality, which simplifies both formal definitions and computational implementations.
- In chapter 2, we will define dependency structures formally as labeled directed graphs, where nodes correspond to words (including root) and labeled arcs correspond to typed dependency relations.

![Figure 1: Dependency structure for an English sentence](https://i.imgur.com/4o4Z4f4.png)

- The information encoded in a dependency structure representation is different from the information captured in a phrase structure representation, which is the most widely used type of syntactic representation in both theoretical and computational linguistics.
- While the dependency structure represents head-dependent relations between words, classified by functional categories such as subject (SBJ) and object (OBJ), the phrase structure represents the grouping of words into phrases, classified by structural categories such as noun phrase (NP) and verb phrase (VP).
- Dependency parsing refers to examining the dependencies between the words of a sentence to analyze its grammatical structure.
- Based on this, a sentence is broken into several components. The mechanism is based on the concept that there is a direct link between every linguistic unit of a sentence.
- Dependency parsers are used to map the words in a sentence to semantic roles, thereby identifying the syntactic relations between words.
- Dependency parsing is useful for various natural language processing tasks, such as information extraction, machine translation, sentiment analysis, question answering, and text summarization.
- There are different types of dependency parsers, such as transition-based, graph-based, and neural network-based parsers.
- Each type has its own advantages and disadvantages in terms of accuracy, efficiency, and complexity.
- Dependency grammar is a notation used for describing the languages and it is a superset of Regular grammar.
- CFG consists of a finite set of grammar rules having the following four components:
  - Set of Non-Terminals
  - Set of Terminals
  - Set of Productions
  - Start Symbol
- Set of Non-terminals: It is represented by V. The non-terminals are syntactic variables that denote the sets of strings, which helps in defining the language that is generated with the help of grammar.
- Set of Terminals: It is also known as tokens and represented by Σ. Strings are formed with the help of the basic symbols of terminals.
- Set of Productions: It is represented by P. The set gives an idea about how the terminals and nonterminals can be combined. Every production consists of the following components:
  - A non-terminal symbol on the left-hand side
  - An arrow symbol (→)
  - A string of terminals and/or non-terminals on the right-hand side
- Start Symbol: It is represented by S. It is a special non-terminal symbol that appears in the initial production of the grammar.
- An example of a context-free grammar is given below:

```
S → NP VP
NP → Det N
VP → V NP
Det → a | the
N → dog | cat
V → chased | caught
```

- This grammar can generate sentences such as "the dog chased a cat"